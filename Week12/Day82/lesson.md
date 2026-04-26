# Day 82 – Data Cleaning — Nulls, Types & Duplicates

## Learning Objectives
- Detect and handle missing values
- Fix data types
- Remove duplicates and outliers

---

## Detecting Missing Values

```python
import pandas as pd

df.isnull().sum()          # count nulls per column
df.isnull().sum() / len(df)  # proportion
df[df["age"].isnull()]     # rows where age is null
```

---

## Handling Missing Values

```python
# Drop rows with any null
df.dropna()

# Drop rows where specific columns are null
df.dropna(subset=["email", "name"])

# Fill with a constant
df["score"].fillna(0)

# Fill with column mean
df["score"] = df["score"].fillna(df["score"].mean())

# Forward-fill (useful for time series)
df["price"] = df["price"].ffill()
```

---

## Fixing Data Types

```python
df["age"]   = df["age"].astype(int)
df["price"] = pd.to_numeric(df["price"], errors="coerce")   # non-numeric → NaN
df["date"]  = pd.to_datetime(df["date"], format="%Y-%m-%d")
```

---

## String Cleaning

```python
df["name"]  = df["name"].str.strip().str.title()
df["email"] = df["email"].str.lower()
df["phone"] = df["phone"].str.replace(r"\D", "", regex=True)  # keep digits only
```

---

## Removing Duplicates

```python
df.duplicated().sum()                  # count duplicates
df.drop_duplicates()                   # remove exact duplicates
df.drop_duplicates(subset=["email"])   # dedupe on specific column
```

---

## Key Takeaways
- Always check `isnull().sum()` before any analysis — hidden nulls break calculations
- `errors="coerce"` in `pd.to_numeric` converts bad values to NaN instead of crashing
- Fix dtypes early — date strings as objects waste memory and break time operations

---

## Exercises
See `exercises.py`
