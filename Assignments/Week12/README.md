<!-- assignments-nav -->
[🏠 Home](../../) | [📚 Week 12 Lessons — Pandas & Data Visualisation](../../Week12/)

---
<!-- assignments-nav -->

# Week 12 Assignments — Pandas & Data Visualisation

**Days 78–84 · Topics: Series, DataFrame, Exploration, Filtering, GroupBy, Cleaning, Matplotlib, Seaborn**

---

## Assignments

### Day 78 — Intro to pandas
- Create a DataFrame of 10 countries with population, GDP, and continent
- Print `shape`, `dtypes`, `describe()`, and `info()`
- Access 3 rows using `.iloc` and a specific country using `.loc`

### Day 79 — Loading & Exploring
- Load a CSV of your choice (Kaggle has thousands of free datasets)
- Print head, tail, value_counts for at least 2 columns, and nunique for each column
- Write a 5-sentence "data profile" describing what you found

### Day 80 — Filtering & Sorting
- Filter the dataset to rows matching at least 2 conditions
- Add a computed column using `.apply(lambda …)`
- Sort by 2 columns and display the top 10 rows

### Day 81 — GroupBy & Merging
- Produce a `groupby` summary with at least 3 aggregation functions
- Create a pivot table
- Merge two DataFrames on a shared key and verify the row count

### Day 82 — Data Cleaning
- Find and report null counts per column
- Fill or drop nulls with a justification comment
- Fix at least one dtype; normalise at least one string column

### Day 83 — Visualisation
- Create a bar chart, line chart, and histogram from your dataset
- Create one Seaborn plot (boxplot, violin, or scatterplot with hue)
- Save all charts as PNG files with descriptive names

### Day 84 — Project: Dashboard
- Build a 4-panel dashboard using `plt.subplots`
- Include: bar, line, pie (or horizontal bar), and a heatmap
- Save the final dashboard as `dashboard.png` at 150 dpi

---

## Grading Criteria

| Criteria | Points |
|----------|--------|
| Data exploration thorough | 25 |
| Correct use of groupby/merge | 25 |
| Data cleaning justified | 25 |
| Charts labelled and saved | 25 |
| **Total** | **100** |
