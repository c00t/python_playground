import csv
from pathlib import Path

file_path = Path.cwd() / "CSVwithHeader.csv"
with file_path.open(mode="r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)
    print(reader.fieldnames)
    for row in reader:
        print(row)

