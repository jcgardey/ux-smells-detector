from openai import OpenAI
import re

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
)


import csv
import time
import json

#prompt = "Necesito que actues como un modelo de prediccion. Te voy a indicar una serie de issues reportados por otros usuarios (separados por titulo y descripcion) en un repositorio de código de github y necesito que me indiques si cada uno corresponde a un UX smell o no. Los UX smells indican deficiencias en la experiencia de los usuarios, no son bugs ni feature requests. Reportan problemas de UX que pueden mejorarse sin modificar la funcionalidad de la aplicacion. Si consideras que es un UX smell indicame con cual de los siguientes aspectos se relaciona: efficiency, flexibility, informativeness and intuitiveness. Responde en formato json (sin texto adicional) con un objeto por cada issue las siguientes claves: 'is_ux_smell' (boolean), 'reasoning' (string) explicando brevemente el razonamiento con no más de 25 palabras y 'aspect' con el aspecto seleccionado."

def read_prompt():
    try:
        with open('prompt.md', 'r', encoding='utf-8') as f:
            return f.read().strip()
    except FileNotFoundError:
        raise Exception("prompt.md file not found")

prompt = read_prompt()

def predict_ux_smell(issue_body, model):
    chat_completion = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "system",
                "content": prompt
            },
            {"role": "user", "content": issue_body}
        ],
    )
    response = chat_completion.choices[0].message.content.split("<")[0]
    print(response)
    raw_json = re.search(r'\[[^\]]+\]', response)
    try:
        parsed = json.loads(raw_json.group(0))
    except Exception:
        raise ValueError("Could not parse response")
    return parsed


