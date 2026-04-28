<!-- nav -->
[← Day 80](../Day80/lesson.md) | [🏠 Home](../../) | [Day 82 →](../Day82/lesson.md)

---
<!-- nav -->

# Day 81 – Grouping, Aggregation & Merging

## Learning Objectives
- Use `groupby` to split-apply-combine data
- Apply multiple aggregation functions at once
- Merge two DataFrames with `merge` and `join`

---

## `groupby` + `agg`

```python
import pandas as pd

# Single aggregation
df.groupby("department")["salary"].mean()

# Multiple aggregations
df.groupby("department")["salary"].agg(["mean", "max", "count"])

# Named aggregations
df.groupby("region").agg(
    total_sales = ("sales", "sum"),
    avg_sales   = ("sales", "mean"),
    reps        = ("name", "count"),
)
```

---

## Pivot Tables

```python
pivot = df.pivot_table(
    values  = "sales",
    index   = "region",
    columns = "quarter",
    aggfunc = "sum",
    fill_value = 0,
)
print(pivot)
```

---

## `merge` — SQL-style Join

```python
# Inner join (default)
merged = pd.merge(orders, customers, on="customer_id")

# Left join
merged = pd.merge(orders, customers, on="customer_id", how="left")

# Join on differently-named keys
merged = pd.merge(orders, products, left_on="prod_id", right_on="id")
```

---

## `concat` — Stack DataFrames

```python
# Stack rows vertically
combined = pd.concat([df_q1, df_q2, df_q3], ignore_index=True)

# Stack columns horizontally
wide = pd.concat([df_a, df_b], axis=1)
```

---

## Key Takeaways
- `groupby().agg()` replaces many manual loops — it's faster and more readable
- Use named aggregations `agg(col=(source, func))` for clean output column names
- `merge()` mirrors SQL JOIN — default is inner join; specify `how=` to change it

---

## Exercises
See `exercises.py`

---

<!-- nav -->
[📝 Exercises](exercises.py) | [← Day 80](../Day80/lesson.md) | [Day 82 →](../Day82/lesson.md)
<!-- nav -->
