<!-- nav -->
[← Day 83](../Day83/lesson.md) | [🏠 Home](../../) | [Day 85 →](../../Week13/Day85/lesson.md)

---
<!-- nav -->

# Day 84 – Project: Sales Analysis Dashboard

## What You're Building
A Python script that reads a CSV of sales data, cleans it, analyses it, and outputs a multi-panel chart dashboard.

---

## Learning Objectives
- Apply data cleaning, groupby, and visualisation in a single pipeline
- Build a multi-panel `plt.subplots` figure
- Save the finished dashboard as a PNG

---

## Sample Dataset Schema

```
date,region,product,quantity,price
2026-01-05,North,Widget,10,9.99
2026-01-07,South,Gadget,5,24.99
...
```

---

## Analysis Steps

1. Load and clean the data
2. Add a `revenue` column: `quantity * price`
3. Group by `region` → total revenue
4. Group by `product` → total units sold
5. Group by `date` (month) → monthly revenue trend
6. Plot all three as a 3-panel dashboard

---

## Dashboard Layout

```python
import matplotlib.pyplot as plt

fig, axes = plt.subplots(1, 3, figsize=(18, 5))
fig.suptitle("Sales Dashboard", fontsize=16, fontweight="bold")

# Panel 1 — Revenue by Region (bar)
axes[0].bar(region_df.index, region_df["revenue"], color="steelblue")
axes[0].set_title("Revenue by Region")

# Panel 2 — Units Sold by Product (horizontal bar)
axes[1].barh(product_df.index, product_df["quantity"], color="coral")
axes[1].set_title("Units Sold by Product")

# Panel 3 — Monthly Revenue Trend (line)
axes[2].plot(monthly_df.index, monthly_df["revenue"], marker="o", color="green")
axes[2].set_title("Monthly Revenue")

plt.tight_layout()
plt.savefig("dashboard.png", dpi=150)
plt.show()
```

---

## Stretch Goals
- Use Seaborn styling: `sns.set_theme(style="whitegrid")`
- Add percentage labels on the bar charts
- Export summary stats to a Markdown table

---

## Exercises
See `exercises.py`

---

<!-- nav -->
[📝 Exercises](exercises.py) | [← Day 83](../Day83/lesson.md) | [Day 85 →](../../Week13/Day85/lesson.md)
<!-- nav -->
