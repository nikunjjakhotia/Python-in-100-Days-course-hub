# Day 83 – Matplotlib & Seaborn Visualisation
# Run: pip install matplotlib seaborn
# Charts are saved as .png files; plt.show() opens them interactively if available.

import pandas as pd
import matplotlib
matplotlib.use("Agg")   # non-interactive backend for script mode
import matplotlib.pyplot as plt

try:
    import seaborn as sns
    HAS_SEABORN = True
except ImportError:
    HAS_SEABORN = False
    print("seaborn not installed — skipping seaborn exercises. pip install seaborn")

import io, os

CSV = """month,region,sales
Jan,North,12000
Feb,North,13500
Mar,North,11000
Jan,South,9000
Feb,South,11200
Mar,South,14000
"""
df = pd.read_csv(io.StringIO(CSV))
monthly = df.groupby("month")["sales"].sum().reset_index()
by_region = df.groupby("region")["sales"].sum()


# Exercise 1: Bar chart — total sales by region.

fig, ax = plt.subplots(figsize=(7, 4))
ax.bar(by_region.index, by_region.values, color=["steelblue","coral"])
ax.set_title("Total Sales by Region")
ax.set_ylabel("Sales ($)")
plt.tight_layout()
plt.savefig("ex1_bar.png")
plt.close()
print("Saved ex1_bar.png")


# Exercise 2: Line chart — monthly sales trend.

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(monthly["month"], monthly["sales"], marker="o", color="green")
ax.set_title("Monthly Sales Trend")
ax.set_ylabel("Sales ($)")
plt.tight_layout()
plt.savefig("ex2_line.png")
plt.close()
print("Saved ex2_line.png")


# Exercise 3 (Seaborn): Scatter plot with hue.

if HAS_SEABORN:
    tips = sns.load_dataset("tips")
    fig, ax = plt.subplots(figsize=(7, 4))
    sns.scatterplot(data=tips, x="total_bill", y="tip", hue="sex", ax=ax)
    ax.set_title("Tips vs Total Bill")
    plt.tight_layout()
    plt.savefig("ex3_scatter.png")
    plt.close()
    print("Saved ex3_scatter.png")


# Exercise 4 (Seaborn): Box plot — tip distribution by day.

if HAS_SEABORN:
    fig, ax = plt.subplots(figsize=(7, 4))
    sns.boxplot(data=tips, x="day", y="tip", ax=ax)
    ax.set_title("Tip Distribution by Day")
    plt.tight_layout()
    plt.savefig("ex4_box.png")
    plt.close()
    print("Saved ex4_box.png")


# Clean up
for f in ["ex1_bar.png","ex2_line.png","ex3_scatter.png","ex4_box.png"]:
    if os.path.exists(f):
        os.remove(f)
print("Cleaned up chart files.")
