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
model = "meta-llama/llama-3.3-70b-instruct:free"
# Read from issues.csv, write to issues_with_predictions.csv with model response column
input_csv = 'issues.csv'
# Normalize model string by replacing '/' and ':' with spaces
output_csv = f'issues_with_predictions_{ re.sub(r"[/:]", " ", model)}.csv'


import re


def issues_to_string(issues):
    result = ""
    for issue in issues:
        title = issue.get('title', 'No Title')
        body = issue.get('body', 'No Description')
        result += f"Título: {title}\nDescripcion: {body}\n---\n"
    return result

reader_rows = []
with open(input_csv, newline='', encoding='utf-8') as csvfile_in:
    reader = csv.DictReader(csvfile_in)
    reader_rows = list(reader)

# Prepare to append to output CSV; write header only if file doesn't exist or is empty
fieldnames = ['id', 'title', 'ux_smell', 'url', 'reasoning']
try:
    # 'a' will create the file if it doesn't exist
    open_mode = 'a'
    with open(output_csv, open_mode, newline='', encoding='utf-8') as csvfile_out:
        writer = csv.DictWriter(csvfile_out, fieldnames=fieldnames)
        # write header if file was just created or is empty
        csvfile_out.seek(0, 2)  # move to end of file
        if csvfile_out.tell() == 0:
            writer.writeheader()
        try:
            bulk_size = 50
            bulk_qty = len(reader_rows) // bulk_size + (1 if len(reader_rows) % bulk_size != 0 else 0)
            for b in range(bulk_qty):
                print(f"### Processing bulk {b + 1}/{bulk_qty} ###")
                current_issue_i = b * bulk_size
                result = predict_ux_smell(issues_to_string(reader_rows[current_issue_i:current_issue_i + bulk_size]), model)
                #result = reader_rows[current_issue_i:current_issue_i + bulk_size]
                for issue in result:
                    print(f"Issue ID: {reader_rows[current_issue_i]['issueId']}")
                    writer.writerow({'id': reader_rows[current_issue_i]['issueId'], 'title': reader_rows[current_issue_i]['title'], 'ux_smell': issue.get('ux_smell', None), 'url': reader_rows[current_issue_i].get('htmlUrl', ''), 'reasoning': issue.get('reasoning')})
                    current_issue_i += 1
        except Exception as e:
            print(f"Error: {e}")
except Exception as e:
    print(f"Failed to append to {output_csv}: {e}")


