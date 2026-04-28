<!-- nav -->
[← Day 77](../../Week11/Day77/lesson.md) | [🏠 Home](../../) | [Day 79 →](../Day79/lesson.md)

---
<!-- nav -->

# Day 78 – Intro to pandas — Series & DataFrame

## Learning Objectives
- Understand the difference between a `Series` and a `DataFrame`
- Create them from lists, dicts, and CSV files
- Access columns and rows

---

## Install

```bash
pip install pandas
```

---

## Series — 1-D Labelled Array

```python
import pandas as pd

s = pd.Series([10, 20, 30, 40], index=["a", "b", "c", "d"])
print(s)
print(s["b"])      # 20
print(s[s > 15])   # filter
```

---

## DataFrame — 2-D Labelled Table

```python
data = {
    "name":  ["Alice", "Bob", "Carol"],
    "age":   [25, 30, 28],
    "score": [88.5, 92.0, 79.3],
}
df = pd.DataFrame(data)
print(df)
print(df.shape)        # (3, 3)
print(df.dtypes)
print(df.info())
print(df.describe())
```

---

## Accessing Data

```python
# Column
print(df["name"])
print(df[["name", "score"]])   # multiple columns

# Row by label — .loc
print(df.loc[1])               # row with index 1

# Row by position — .iloc
print(df.iloc[0])              # first row
print(df.iloc[1:3, 0:2])       # slice rows and columns
```

---

## From CSV

```python
df = pd.read_csv("data.csv")
df.to_csv("output.csv", index=False)
```

---

## Key Takeaways
- A `Series` is a 1-D array with an index; a `DataFrame` is a collection of `Series`
- `.loc[]` uses labels; `.iloc[]` uses integer positions
- `.info()` and `.describe()` are the first two things to call on a new dataset

---

## Exercises
See `exercises.py`

---

<!-- nav -->
[📝 Exercises](exercises.py) | [← Day 77](../../Week11/Day77/lesson.md) | [Day 79 →](../Day79/lesson.md)
<!-- nav -->
