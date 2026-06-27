import csv
import sys
from collections import Counter

def analyze_csv(file_path):
    with open(file_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    print("总行数:", len(rows))
    print("列名:", reader.fieldnames)

    empty_count = Counter()
    for row in rows:
        for key, value in row.items():
            if value is None or value.strip() == "":
                empty_count[key] += 1

    print("空值统计:")
    for col in reader.fieldnames:
        print(f"  {col}: {empty_count[col]}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python main.py <csv文件名>")
    else:
        analyze_csv(sys.argv[1])