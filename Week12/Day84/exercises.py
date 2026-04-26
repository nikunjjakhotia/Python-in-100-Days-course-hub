# Day 84 – Project: Sales Analysis Dashboard

import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import io, os

# ─── Sample dataset ──────────────────────────────────────────────────────────

CSV = """date,region,product,quantity,price
2026-01-05,North,Widget,10,9.99
2026-01-07,South,Gadget,5,24.99
2026-01-12,East,Widget,8,9.99
2026-01-15,West,Sprocket,15,4.49
2026-02-03,North,Gadget,3,24.99
2026-02-10,South,Widget,12,9.99
2026-02-14,East,Gadget,6,24.99
2026-02-20,West,Widget,20,9.99
2026-03-01,North,Sprocket,25,4.49
2026-03-08,South,Widget,9,9.99
2026-03-15,East,Sprocket,18,4.49
2026-03-22,West,Gadget,4,24.99
"""

# ─── Load & clean ─────────────────────────────────────────────────────────────

df = pd.read_csv(io.StringIO(CSV))
df["date"]    = pd.to_datetime(df["date"])
df["revenue"] = (df["quantity"] * df["price"]).round(2)

print("Dataset loaded:")
print(df.head())
print(f"\nTotal revenue: ${df['revenue'].sum():,.2f}")

# ─── Aggregations ─────────────────────────────────────────────────────────────

region_df  = df.groupby("region")["revenue"].sum().sort_values(ascending=False)
product_df = df.groupby("product")["quantity"].sum().sort_values()
monthly_df = df.resample("ME", on="date")["revenue"].sum()

print("\nRevenue by region:\n", region_df)
print("\nUnits by product:\n", product_df)
print("\nMonthly revenue:\n", monthly_df)

# ─── Dashboard ────────────────────────────────────────────────────────────────

fig, axes = plt.subplots(1, 3, figsize=(18, 5))
fig.suptitle("Sales Dashboard — Q1 2026", fontsize=16, fontweight="bold")

# Panel 1 — Revenue by Region
axes[0].bar(region_df.index, region_df.values, color="steelblue")
axes[0].set_title("Revenue by Region ($)")
axes[0].set_ylabel("Revenue")
for i, v in enumerate(region_df.values):
    axes[0].text(i, v + 1, f"${v:.0f}", ha="center", fontsize=9)

# Panel 2 — Units Sold by Product (horizontal bar)
axes[1].barh(product_df.index, product_df.values, color="coral")
axes[1].set_title("Units Sold by Product")
axes[1].set_xlabel("Units")

# Panel 3 — Monthly Revenue Trend
axes[2].plot(monthly_df.index.strftime("%b"), monthly_df.values,
             marker="o", color="green", linewidth=2)
axes[2].set_title("Monthly Revenue Trend")
axes[2].set_ylabel("Revenue ($)")

plt.tight_layout()
plt.savefig("dashboard.png", dpi=150)
plt.close()
print("\nDashboard saved as dashboard.png")

if os.path.exists("dashboard.png"):
    os.remove("dashboard.png")
