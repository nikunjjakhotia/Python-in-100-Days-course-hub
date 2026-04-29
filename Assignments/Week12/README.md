<!-- assignments-nav -->
[🏠 Home](../../) | [📚 Week 12 Lessons — Pandas & Data Visualisation](../../Week12/)

---
<!-- assignments-nav -->

# Week 12 Assignment: Build a Sales Analysis Dashboard

**Days 78–84 · Topics: pandas Series & DataFrame, Exploration, Filtering, GroupBy, Data Cleaning, Matplotlib, Seaborn**

Using the pandas and visualisation skills from Days 78–84, load a CSV dataset of your choice, clean it, analyse it, and produce a publication-ready dashboard image.

## What to Build
- Load a CSV with at least 200 rows and print `shape`, `dtypes`, `describe()`, and null counts per column
- Clean the data: drop or fill nulls with a justification comment, fix dtypes, normalise at least one string column
- A GroupBy summary aggregated by at least two dimensions (e.g. region + product category), exported to `summary.csv`
- A 4-panel matplotlib figure using `plt.subplots(2, 2)`: bar chart, line chart, histogram, and a Seaborn heatmap — saved as `dashboard.png` at 150 dpi
- A 5-sentence data profile written as a docstring at the top of your script describing what you found
