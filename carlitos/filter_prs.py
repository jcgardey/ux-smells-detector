import json
import csv
import sys

def main():
    try:
        with open('carlitos/all_issues.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print(f"Error reading input json: {e}")
        return
        
    # Filtrar solo los que sean "Issues" regulares usando la URL (evitando "/pull/")
    filtered = [item for item in data if '/issues/' in item.get('URL', '')]
    
    print(f"Total de items antes de filtrar: {len(data)}")
    print(f"Total de issues después de remover Pull Requests: {len(filtered)}")
    
    with open('carlitos/issues_only.json', 'w', encoding='utf-8') as f:
        json.dump(filtered, f, indent=2, ensure_ascii=False)
        
    if filtered:
        keys = filtered[0].keys()
        with open('carlitos/issues_only.csv', 'w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=keys)
            writer.writeheader()
            writer.writerows(filtered)
            
    # Count open vs closed
    open_count = sum(1 for x in filtered if x.get('State') == 'open')
    closed_count = sum(1 for x in filtered if x.get('State') == 'closed')
    
    qc_report = f"""repo=eclipse-platform/eclipse.platform.ui
fetched_total_issues={len(filtered)}
fetched_open_issues={open_count}
fetched_closed_issues={closed_count}
notes=Filtered locally from all_issues.json to avoid GitHub API rate limits. Removed all Pull Requests.
"""
    with open('carlitos/qc_report_issues_only.txt', 'w', encoding='utf-8') as f:
        f.write(qc_report)
        
    print(f"Abiertos: {open_count}, Cerrados: {closed_count}")
    print("Archivos generados: carlitos/issues_only.csv, carlitos/issues_only.json, carlitos/qc_report_issues_only.txt")

if __name__ == "__main__":
    main()
