# Day 79 – Loading & Exploring Data

import pandas as pd
import io

# Sample CSV data (inline so no file needed)
CSV = """name,age,city,salary,department
Alice,29,New York,90000,Engineering
Bob,34,Chicago,75000,Marketing
Carol,27,New York,95000,Engineering
Dave,41,Austin,110000,Management
Eve,31,Chicago,82000,Marketing
Frank,26,New York,88000,Engineering
Grace,38,Austin,72000,HR
Henry,45,Chicago,120000,Management
"""

df = pd.read_csv(io.StringIO(CSV))


# Exercise 1: Print shape, dtypes, and first 3 rows.

# Solution:
print("Shape:", df.shape)
print("\nDtypes:\n", df.dtypes)
print("\nHead(3):\n", df.head(3))


# Exercise 2: Print value_counts for the 'city' and 'department' columns.

# Solution:
print("\nCity counts:\n", df["city"].value_counts())
print("\nDepartment counts:\n", df["department"].value_counts())


# Exercise 3: Print the number of unique cities and the unique city names.

# Solution:
print("\nUnique cities:", df["city"].nunique())
print("Cities:", df["city"].unique())


# Exercise 4: Print a random sample of 3 rows.

# Solution:
print("\nRandom sample:\n", df.sample(3, random_state=42))


# Exercise 5: Sort by salary descending and show top 3 earners.

# Solution:
print("\nTop 3 earners:\n", df.sort_values("salary", ascending=False).head(3)[["name","department","salary"]])
