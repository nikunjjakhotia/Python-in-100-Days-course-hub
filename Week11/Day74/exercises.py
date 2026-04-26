# Day 74 – Automating CSV Reports

import csv, os
from pathlib import Path

DATA_DIR = Path("csv_data")
DATA_DIR.mkdir(exist_ok=True)


# Create sample sales CSV files
SALES_DATA = [
    ["name", "region", "sales"],
    ["Alice",   "North",  "12000"],
    ["Bob",     "South",   "9500"],
    ["Carol",   "North",  "15000"],
    ["Dave",    "East",    "8750"],
    ["Eve",     "West",   "11200"],
    ["Frank",   "South",  "13400"],
]

with open(DATA_DIR / "sales_q1.csv", "w", newline="") as f:
    csv.writer(f).writerows(SALES_DATA)

with open(DATA_DIR / "sales_q2.csv", "w", newline="") as f:
    extra = SALES_DATA[:1] + [["Grace", "East", "16000"], ["Henry", "West", "9000"]]
    csv.writer(f).writerows(extra)


# Exercise 1: Read sales_q1.csv and print each row as a dict.

# Solution:
with open(DATA_DIR / "sales_q1.csv", newline="") as f:
    for row in csv.DictReader(f):
        print(row)


# Exercise 2: Calculate total and average sales from sales_q1.csv.

# Solution:
with open(DATA_DIR / "sales_q1.csv", newline="") as f:
    amounts = [float(r["sales"]) for r in csv.DictReader(f)]
total = sum(amounts)
avg   = total / len(amounts)
print(f"\nQ1 Total: ${total:,.0f}  Average: ${avg:,.0f}")


# Exercise 3: Summarise sales by region from sales_q1.csv.

# Solution:
region_totals = {}
with open(DATA_DIR / "sales_q1.csv", newline="") as f:
    for row in csv.DictReader(f):
        r = row["region"]
        region_totals[r] = region_totals.get(r, 0) + float(row["sales"])

print("\nRegion summary (Q1):")
for region, total in sorted(region_totals.items()):
    print(f"  {region}: ${total:,.0f}")


# Exercise 4: Write a region summary CSV from the dict above.

# Solution:
with open(DATA_DIR / "q1_summary.csv", "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=["region", "total"])
    w.writeheader()
    for region, total in region_totals.items():
        w.writerow({"region": region, "total": total})
print("\nWrote q1_summary.csv")
print(list(DATA_DIR.iterdir()))


# Clean up
import shutil
shutil.rmtree(DATA_DIR)
