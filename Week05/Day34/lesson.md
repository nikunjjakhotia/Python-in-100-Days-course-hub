# Day 34 – Real-World Use Cases for Data Structures

## Learning Objectives
- Apply lists, dicts, sets, and comprehensions to realistic problems
- Recognise which data structure best fits a given problem
- Combine multiple structures in a small pipeline

---

## Use Case 1: Inventory Management

```python
inventory = {
    "apple":  {"qty": 50, "price": 0.99},
    "banana": {"qty": 30, "price": 0.49},
    "cherry": {"qty": 10, "price": 3.99},
}

low_stock = [item for item, data in inventory.items() if data["qty"] < 20]
print("Low stock:", low_stock)  # ['cherry']
```

---

## Use Case 2: Deduplicating User Input

```python
tags = ["python", "code", "Python", "tutorial", "code", "AI"]
unique_tags = list({t.lower() for t in tags})
print(unique_tags)
```

---

## Use Case 3: Grouping Data by Category

```python
transactions = [
    {"type": "income", "amount": 2000},
    {"type": "expense", "amount": 500},
    {"type": "income", "amount": 1500},
    {"type": "expense", "amount": 300},
]

from collections import defaultdict
by_type = defaultdict(list)
for t in transactions:
    by_type[t["type"]].append(t["amount"])

for t_type, amounts in by_type.items():
    print(f"{t_type}: total={sum(amounts)}, count={len(amounts)}")
```

---

## Use Case 4: Lookup Table for Fast Access

```python
# O(n) list search
def find_user_list(users, uid):
    for u in users:
        if u["id"] == uid:
            return u

# O(1) dict lookup
users_dict = {u["id"]: u for u in users}
user = users_dict.get(42)
```

---

## Key Takeaways
- Dict lookup is O(1); list search is O(n) — use dicts as indexes
- Sets are ideal for deduplication and membership checks
- Comprehensions + `defaultdict` = powerful one-pass aggregations

---

## Exercises
See `exercises.py`
