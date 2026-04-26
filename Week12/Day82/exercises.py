# Day 82 – Data Cleaning — Nulls, Types & Duplicates

import pandas as pd
import numpy as np
import io

DIRTY_CSV = """name,age,email,score,joined
Alice,29,alice@example.com,88.5,2023-03-01
Bob,,bob@example.com,92,2023-05-15
Carol,27,carol@example.com,,2023-01-10
Dave,41,dave@example.com,74.0,2023-03-01
Eve,31,eve@EXAMPLE.COM,81,2023-07-22
Alice,29,alice@example.com,88.5,2023-03-01
Frank,twenty,frank@example.com,67,2023-09-05
"""

df = pd.read_csv(io.StringIO(DIRTY_CSV))
print("Raw data:")
print(df)
print("\nNull counts:\n", df.isnull().sum())


# Exercise 1: Fix the age column — convert to numeric (coerce errors to NaN),
# then fill missing with median age.

# Solution:
df["age"] = pd.to_numeric(df["age"], errors="coerce")
df["age"] = df["age"].fillna(df["age"].median()).astype(int)
print("\nFixed age:\n", df["age"])


# Exercise 2: Fill missing score with the column mean.

# Solution:
df["score"] = df["score"].fillna(df["score"].mean()).round(1)
print("\nFixed score:\n", df["score"])


# Exercise 3: Normalise the email column to lowercase.

# Solution:
df["email"] = df["email"].str.lower()


# Exercise 4: Parse the joined column as datetime.

# Solution:
df["joined"] = pd.to_datetime(df["joined"])
print("\nJoined dtype:", df["joined"].dtype)


# Exercise 5: Remove duplicate rows (keep first occurrence).

# Solution:
before = len(df)
df = df.drop_duplicates()
print(f"\nDropped {before - len(df)} duplicate row(s)")
print("\nClean data:")
print(df)
