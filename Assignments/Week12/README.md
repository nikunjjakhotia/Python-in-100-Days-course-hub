<!-- assignments-nav -->
[🏠 Home](../../) | [📚 Week 12 Lessons — Pandas & Data Visualisation](../../Week12/)

---
<!-- assignments-nav -->

# Week 12 Assignment — Sales Analysis Dashboard

**Days 78–84 · Topics: pandas Series & DataFrame, Exploration, Filtering, GroupBy, Data Cleaning, Matplotlib, Seaborn**

Load a real-world CSV dataset, clean it, analyse it with pandas, and produce a publication-ready 4-panel dashboard image.

---

## 🎯 What You'll Build

A data analysis script that turns a raw CSV into a polished dashboard PNG — the kind of output you'd present to a manager or include in a portfolio.

---

## 📋 Requirements

1. Load a CSV dataset with **at least 200 rows** — use any free dataset (Kaggle, data.gov, Our World in Data). Print `shape`, `dtypes`, `describe()`, and null counts per column on startup.
2. **Clean the data:** drop or fill nulls with a comment explaining why; cast numeric columns stored as strings; normalise at least one text column (strip whitespace, lowercase or title case).
3. Produce a **GroupBy summary** aggregated by at least two dimensions (e.g. region + product category) — calculate sum, mean, and count; export to `summary.csv`.
4. Build a **4-panel matplotlib figure** using `plt.subplots(2, 2)`:
   - Top-left: bar chart of the top 10 values in a key categorical column
   - Top-right: line chart of a numeric column over time (or by sorted category)
   - Bottom-left: histogram of a continuous variable with `bins=20`
   - Bottom-right: Seaborn heatmap of the correlation matrix
5. Save the figure as `dashboard.png` at **150 dpi** with `bbox_inches="tight"`.
6. Add a `--dataset` CLI argument that accepts a CSV path so the script works with any file, not just your specific dataset.
7. Filter the DataFrame to rows where the main numeric column is **above the 75th percentile** and print the top 5 rows.
8. Write a **5-sentence data profile** as a module-level docstring at the top of the file summarising what you found.

---

## 💡 Hints

- `df.isnull().sum()` shows null counts per column.
- `df.groupby(["col1", "col2"]).agg({"sales": ["sum", "mean", "count"]})` multi-aggregates.
- `df.corr(numeric_only=True)` feeds directly into `sns.heatmap()`.
- `df[df["sales"] > df["sales"].quantile(0.75)]` filters above the 75th percentile.

---

## 📤 How to Submit

1. Save your solution as `Week12_assignment.py` plus `dashboard.png` and `summary.csv` inside this folder.
2. Run the script end-to-end and confirm the PNG looks correct.
3. Share `dashboard.png` on LinkedIn with **#Python100Days** and tag [@nikunjjakhotia](https://www.linkedin.com/in/nikunjjakhotia/).

---

## ✅ Marking Criteria

| Criterion | Marks |
|-----------|-------|
| Dataset loaded and exploration output printed | /10 |
| Data cleaning applied with justification comments | /10 |
| GroupBy summary exported to `summary.csv` | /10 |
| 4-panel dashboard saved as `dashboard.png` at 150 dpi | /15 |
| 5-sentence data profile docstring present | /5 |
| **Total** | **/50** |
