<!-- nav -->
[← Day 73](../Day73/lesson.md) | [🏠 Home](../../) | [Day 75 →](../Day75/lesson.md)

---
<!-- nav -->

# Day 74 – Automating CSV Reports

## Learning Objectives
- Read and write CSV files with the `csv` module
- Generate summary reports programmatically
- Combine file I/O with `pathlib` for batch processing

---

## Reading CSV

```python
import csv

with open("sales.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row["name"], row["amount"])
```

`DictReader` maps each row to a dict using the header row as keys.

---

## Writing CSV

```python
records = [
    {"name": "Alice", "sales": 12000, "region": "North"},
    {"name": "Bob",   "sales":  9500, "region": "South"},
]

with open("report.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["name", "sales", "region"])
    writer.writeheader()
    writer.writerows(records)
```

---

## Generating a Summary Report

```python
from pathlib import Path
import csv

def summarise(input_path: Path) -> dict:
    totals = {}
    with open(input_path, newline="") as f:
        for row in csv.DictReader(f):
            region = row["region"]
            amount = float(row["sales"])
            totals[region] = totals.get(region, 0) + amount
    return totals

summary = summarise(Path("sales.csv"))
for region, total in sorted(summary.items()):
    print(f"{region}: ${total:,.2f}")
```

---

## Batch Processing Multiple Files

```python
from pathlib import Path

for csv_file in Path("data").glob("*.csv"):
    summary = summarise(csv_file)
    out = csv_file.with_suffix("_summary.csv")
    with open(out, "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["region", "total"])
        w.writerows(summary.items())
    print(f"Written: {out}")
```

---

## Key Takeaways
- Always open CSV files with `newline=""` to avoid extra blank lines
- `DictReader` / `DictWriter` are safer than positional reader/writer for real data
- `Path.glob("*.csv")` makes batch processing trivial

---

## Exercises
See `exercises.py`

---

<!-- nav -->
[📝 Exercises](https://github.com/nikunjjakhotia/Python-in-100-Days-course-hub/blob/main/Week11/Day74/exercises.py) | [← Day 73](../Day73/lesson.md) | [Day 75 →](../Day75/lesson.md)
<!-- nav -->
