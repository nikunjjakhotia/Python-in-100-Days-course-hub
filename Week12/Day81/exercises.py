# Day 81 – Grouping, Aggregation & Merging

import pandas as pd
import io

SALES_CSV = """region,product,rep,sales,units
North,Widget,Alice,12000,120
North,Gadget,Bob,8500,34
South,Widget,Carol,15000,150
South,Gadget,Dave,7200,29
East,Widget,Eve,11500,115
East,Sprocket,Frank,3200,64
West,Gadget,Grace,9800,39
West,Widget,Henry,13200,132
"""
REPS_CSV = """rep,email
Alice,alice@co.com
Bob,bob@co.com
Carol,carol@co.com
"""

df    = pd.read_csv(io.StringIO(SALES_CSV))
reps  = pd.read_csv(io.StringIO(REPS_CSV))


# Exercise 1: Total and average sales by region.

# Solution:
print("Sales by region:")
print(df.groupby("region")["sales"].agg(total="sum", avg="mean").round(0))


# Exercise 2: Named aggregation — total sales, avg units, rep count per region.

# Solution:
print("\nRegion summary:")
print(df.groupby("region").agg(
    total_sales = ("sales", "sum"),
    avg_units   = ("units", "mean"),
    reps        = ("rep", "count"),
))


# Exercise 3: Pivot table — sales by product × region.

# Solution:
pivot = df.pivot_table(values="sales", index="product", columns="region",
                       aggfunc="sum", fill_value=0)
print("\nPivot (sales by product × region):\n", pivot)


# Exercise 4: Merge sales df with reps df on 'rep' (left join so all sales rows are kept).

# Solution:
merged = pd.merge(df, reps, on="rep", how="left")
print("\nMerged (with email):")
print(merged[["rep","region","sales","email"]].head())


# Exercise 5: Stack two DataFrames vertically using concat.

# Solution:
df_a = df[df["region"].isin(["North","South"])].copy()
df_b = df[df["region"].isin(["East","West"])].copy()
combined = pd.concat([df_a, df_b], ignore_index=True)
print(f"\nCombined rows: {len(combined)} (original: {len(df)})")
