<!-- nav -->
[← Day 79](../Day79/lesson.md) | [🏠 Home](../../) | [Day 81 →](../Day81/lesson.md)

---
<!-- nav -->

# Day 80 – Filtering, Sorting & Selection

## Learning Objectives
- Filter rows with boolean conditions
- Sort by one or more columns
- Select and rename columns

---

## Boolean Filtering

```python
import pandas as pd

# Single condition
seniors = df[df["age"] >= 65]

# Multiple conditions — use & (and), | (or), ~ (not)
result = df[(df["age"] >= 18) & (df["score"] > 80)]

# isin — match a list of values
result = df[df["country"].isin(["USA", "Canada", "UK"])]

# str methods
result = df[df["name"].str.startswith("A")]
result = df[df["email"].str.contains("gmail")]
```

---

## Sorting

```python
# Sort by one column (ascending by default)
df.sort_values("score")

# Sort descending
df.sort_values("score", ascending=False)

# Sort by multiple columns
df.sort_values(["country", "score"], ascending=[True, False])
```

---

## Selecting & Renaming Columns

```python
# Select subset
subset = df[["name", "score", "age"]]

# Rename
df = df.rename(columns={"name": "full_name", "score": "test_score"})

# Drop columns
df = df.drop(columns=["unnecessary_col"])
```

---

## Adding Computed Columns

```python
df["grade"] = df["score"].apply(lambda s: "A" if s >= 90 else "B" if s >= 80 else "C")
df["age_group"] = pd.cut(df["age"], bins=[0, 18, 35, 60, 120], labels=["child","young","adult","senior"])
```

---

## Key Takeaways
- Boolean indexing: wrap conditions in `()` and use `&`/`|` instead of `and`/`or`
- `sort_values()` never modifies in place — assign back or use `inplace=True`
- `apply(lambda)` is the escape hatch when built-in vectorised operations don't cover the logic

---

## Exercises
See `exercises.py`

---

<!-- nav -->
[📝 Exercises](https://github.com/nikunjjakhotia/Python-in-100-Days-course-hub/blob/main/Week12/Day80/exercises.py) | [← Day 79](../Day79/lesson.md) | [Day 81 →](../Day81/lesson.md)
<!-- nav -->
