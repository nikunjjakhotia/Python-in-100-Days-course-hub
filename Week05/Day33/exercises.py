# Day 33 – Sorting & Filtering

# Exercise 1: Sort a list of words alphabetically, then by length.

# Solution:
words = ["banana", "apple", "cherry", "date", "elderberry", "fig"]
print("Alphabetical:", sorted(words))
print("By length:", sorted(words, key=len))
print("By length desc:", sorted(words, key=len, reverse=True))


# Exercise 2: Sort student dicts by score descending; print name and rank.

# Solution:
students = [
    {"name": "Charlie", "score": 71},
    {"name": "Alice",   "score": 95},
    {"name": "Diana",   "score": 95},
    {"name": "Bob",     "score": 82},
]
ranked = sorted(students, key=lambda s: (-s["score"], s["name"]))
for i, s in enumerate(ranked, 1):
    print(f"{i}. {s['name']}: {s['score']}")


# Exercise 3: Filter products with price between $10 and $50.

# Solution:
products = [
    {"name": "Pen", "price": 2.5},
    {"name": "Notebook", "price": 12.0},
    {"name": "Laptop", "price": 999.0},
    {"name": "Mouse", "price": 35.0},
    {"name": "USB Cable", "price": 8.0},
    {"name": "Keyboard", "price": 45.0},
]
affordable = [p for p in products if 10 <= p["price"] <= 50]
for p in affordable:
    print(f"{p['name']}: ${p['price']:.2f}")


# Exercise 4: Find the top 3 highest-scoring students.

# Solution:
top3 = sorted(students, key=lambda s: s["score"], reverse=True)[:3]
print("\nTop 3:", [s["name"] for s in top3])


# Exercise 5: Sort a list of file names by their extension, then name.

# Solution:
files = ["report.pdf", "script.py", "data.csv", "notes.md", "app.py", "budget.csv"]
files_sorted = sorted(files, key=lambda f: (f.split(".")[-1], f))
print("\nBy extension:", files_sorted)
