<!-- nav -->
[← Day 82](../Day82/lesson.md) | [🏠 Home](../../) | [Day 84 →](../Day84/lesson.md)

---
<!-- nav -->

# Day 83 – Matplotlib & Seaborn Visualisation

## Learning Objectives
- Create bar, line, scatter, and histogram charts with Matplotlib
- Produce publication-ready plots with Seaborn
- Customise labels, titles, and figure size

---

## Install

```bash
pip install matplotlib seaborn
```

---

## Matplotlib Basics

```python
import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 15, 7, 20, 13]

plt.figure(figsize=(8, 4))
plt.plot(x, y, marker="o", color="steelblue", label="Sales")
plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Units Sold")
plt.legend()
plt.tight_layout()
plt.savefig("sales.png")   # save before show
plt.show()
```

---

## Common Chart Types

```python
# Bar chart
plt.bar(categories, values, color="coral")

# Histogram
plt.hist(data, bins=20, color="steelblue", edgecolor="white")

# Scatter
plt.scatter(x, y, c=colors, s=sizes, alpha=0.6)
```

---

## Seaborn — Higher-Level Interface

```python
import seaborn as sns
import pandas as pd

tips = sns.load_dataset("tips")

# Distribution
sns.histplot(tips["total_bill"], kde=True)

# Relationship
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="sex")

# Category
sns.boxplot(data=tips, x="day", y="total_bill", hue="sex")

# Heatmap (correlation)
sns.heatmap(tips.corr(numeric_only=True), annot=True, cmap="coolwarm")

plt.tight_layout()
plt.show()
```

---

## Key Takeaways
- Always set `figsize` to avoid tiny default charts
- Seaborn builds on Matplotlib — you can mix both in the same figure
- `plt.tight_layout()` prevents labels from being cut off

---

## Exercises
See `exercises.py`

---

<!-- nav -->
[📝 Exercises](exercises.py) | [← Day 82](../Day82/lesson.md) | [Day 84 →](../Day84/lesson.md)
<!-- nav -->
