# Day 80 – Filtering, Sorting & Selection

import pandas as pd
import io

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


# Exercise 1: Filter employees in Engineering with salary > 85000.

# Solution:
eng_high = df[(df["department"] == "Engineering") & (df["salary"] > 85_000)]
print("Engineering, salary > 85k:\n", eng_high[["name","salary"]])


# Exercise 2: Filter employees whose city is Chicago OR Austin.

# Solution:
print("\nChicago or Austin:\n", df[df["city"].isin(["Chicago","Austin"])][["name","city"]])


# Exercise 3: Add a 'seniority' column — "Senior" if age >= 35, else "Junior".

# Solution:
df["seniority"] = df["age"].apply(lambda a: "Senior" if a >= 35 else "Junior")
print("\nSeniority counts:\n", df["seniority"].value_counts())


# Exercise 4: Sort by department (asc) then salary (desc).

# Solution:
sorted_df = df.sort_values(["department","salary"], ascending=[True, False])
print("\nSorted:\n", sorted_df[["name","department","salary"]])


# Exercise 5: Select only name, department, and salary; rename salary → annual_pay.

# Solution:
subset = df[["name","department","salary"]].rename(columns={"salary":"annual_pay"})
print("\nSubset:\n", subset)
