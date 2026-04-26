# Day 79 – Loading & Exploring Data

## Learning Objectives
- Load data from CSV, JSON, and dict sources
- Use `head`, `tail`, `sample`, `value_counts`, and `nunique`
- Understand index types and reset the index

---

## Loading Data

```python
import pandas as pd

# From CSV
df = pd.read_csv("data.csv")

# From JSON
df = pd.read_json("data.json")

# From a list of dicts (common when working with APIs)
records = [{"city": "NYC", "pop": 8.3e6}, {"city": "LA", "pop": 4.0e6}]
df = pd.DataFrame(records)
```

---

## First Look

```python
df.head(5)          # first 5 rows
df.tail(3)          # last 3 rows
df.sample(5)        # 5 random rows
df.shape            # (rows, cols)
df.columns          # column names
df.dtypes           # data types per column
df.info()           # non-null counts + dtypes
df.describe()       # statistics for numeric columns
```

---

## Value Counts

```python
df["category"].value_counts()         # frequency of each value
df["category"].value_counts(normalize=True)   # as proportions
```

---

## Unique Values

```python
df["country"].unique()     # array of unique values
df["country"].nunique()    # count of unique values
```

---

## Resetting the Index

```python
df = df.reset_index(drop=True)   # reassign 0-based integer index
```

---

## Key Takeaways
- `head()` / `tail()` / `sample()` are your first exploratory tools
- `value_counts()` reveals distribution without plotting
- `nunique()` quickly tells you whether a column is high- or low-cardinality

---

## Exercises
See `exercises.py`
