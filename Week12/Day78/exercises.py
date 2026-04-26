# Day 78 – Intro to pandas — Series & DataFrame

import pandas as pd

# Exercise 1: Create a Series of monthly temperatures and print max, min, mean.

# Solution:
temps = pd.Series([22, 25, 28, 35, 38, 40, 39, 37, 32, 27, 23, 20],
                  index=["Jan","Feb","Mar","Apr","May","Jun",
                         "Jul","Aug","Sep","Oct","Nov","Dec"])
print("Max:", temps.max(), " Min:", temps.min(), " Mean:", round(temps.mean(), 1))
print("Hottest month:", temps.idxmax())


# Exercise 2: Create a DataFrame of 5 students with name, grade, and score.

# Solution:
df = pd.DataFrame({
    "name":  ["Alice", "Bob", "Carol", "Dave", "Eve"],
    "grade": ["A",     "B",   "A",     "C",    "B"],
    "score": [95.0,    82.0,  91.5,    67.0,   78.5],
})
print("\n", df)
print("\nDtypes:\n", df.dtypes)
print("\nDescribe:\n", df.describe())


# Exercise 3: Access the score column and print rows where score > 80.

# Solution:
print("\nScore > 80:")
print(df[df["score"] > 80])


# Exercise 4: Access the first 3 rows using iloc and the row for Bob using loc.

# Solution:
print("\nFirst 3 rows (iloc):")
print(df.iloc[:3])
bob_idx = df[df["name"] == "Bob"].index[0]
print("\nBob (loc):", df.loc[bob_idx].to_dict())


# Exercise 5: Add a column 'passed' (True if score >= 70).

# Solution:
df["passed"] = df["score"] >= 70
print("\nWith passed column:")
print(df)
