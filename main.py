import csv
import sys
import json
from collections import Counter

def analyze_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    empty_count = Counter()
    for row in rows:
        for key, value in row.items():
            if value is None or value.strip() == "":
                empty_count[key] += 1

    result = {
        "row_count": len(rows),
        "columns": reader.fieldnames,
        "empty_counts": dict(empty_count)
    }

    print(json.dumps(result, ensure_ascii=False, indent=2))
    return result

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python main.py <csv文件名>")
    else:
        analyze_csv(sys.argv[1])