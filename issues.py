import os
from openai import OpenAI
from test import predict_ux_smell

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key="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",
)


import csv
import time
import random
import re

#model = "deepseek/deepseek-chat-v3.1:free"
#model = "openai/gpt-oss-20b:free"
model = "google/gemini-2.0-flash-exp:free"

# Read from issues.csv, write to issues_with_predictions.csv with model response column
input_csv = 'issues.csv'
# Normalize model string by replacing '/' and ':' with spaces
output_csv = f'issues_with_predictions_{ re.sub(r"[/:]", " ", model)}.csv'


import re


def get_existing_ids(output_csv):
    existing_ids = []
    if not os.path.exists(output_csv):
        return existing_ids
    try:
        with open(output_csv, newline='', encoding='utf-8') as csvfile_out:
            reader = csv.DictReader(csvfile_out)
            for row in reader:
                existing_ids.append(row['id'])
    except FileNotFoundError:
        return []
    return existing_ids

def issues_to_string(issues):
    result = ""
    for issue in issues:
        title = issue.get('title', 'No Title')
        body = issue.get('body', 'No Description')
        result += f"Título: {title}\nDescripción: {body}\n---\n"
    return result

reader_rows = []
existing_issues_ids = get_existing_ids(output_csv)
with open(input_csv, newline='', encoding='utf-8') as csvfile_in:
    reader = csv.DictReader(csvfile_in)
    reader_rows = list(reader)

# Prepare to append to output CSV; write header only if file doesn't exist or is empty
fieldnames = ['id', 'title', 'is_ux_smell', 'aspect', 'url', 'reasoning']
try:
    # 'a' will create the file if it doesn't exist
    open_mode = 'a'
    with open(output_csv, open_mode, newline='', encoding='utf-8') as csvfile_out:
        writer = csv.DictWriter(csvfile_out, fieldnames=fieldnames)
        # write header if file was just created or is empty
        csvfile_out.seek(0, 2)  # move to end of file
        if csvfile_out.tell() == 0:
            writer.writeheader()
        for i in range(5):
            row = random.choice(reader_rows)
            issue_id = row.get('issueId')
            issue_body = row.get('body')
            if not issue_id or issue_id in existing_issues_ids:
                continue
            issue_title = row.get('title', '')
            prompt = f"Título: {issue_title}\n\nDescripción: {issue_body}"
            try:
                result = predict_ux_smell(prompt, model)
                print(f"Issue ID: {issue_id}, Model Response: {result}")
                writer.writerow({'id': issue_id, 'title': row['title'], 'is_ux_smell': result.get('is_ux_smell'), 'aspect': result.get('aspect', None), 'url': row.get('htmlUrl', ''), 'reasoning': result.get('reasoning')})
            except Exception as e:
                print(f"Issue ID: {issue_id}, Error: {e}")
            time.sleep(1)  # Add a 1-second delay between requests
except Exception as e:
    print(f"Failed to append to {output_csv}: {e}")


