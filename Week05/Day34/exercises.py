# Day 34 – Real-World Use Cases for Data Structures
from collections import defaultdict

# Exercise 1: Find products with low stock (qty < 20) from an inventory dict.

# Solution:
inventory = {
    "apple":  {"qty": 50, "price": 0.99},
    "banana": {"qty": 15, "price": 0.49},
    "cherry": {"qty": 8,  "price": 3.99},
    "mango":  {"qty": 25, "price": 1.29},
}
low_stock = [item for item, data in inventory.items() if data["qty"] < 20]
print("Low stock items:", low_stock)


# Exercise 2: Deduplicate and normalise a list of tags (lowercase, no duplicates).

# Solution:
raw_tags = ["Python", "python", "CODE", "code", "AI", "ai", "tutorial"]
clean_tags = sorted({tag.lower() for tag in raw_tags})
print("Clean tags:", clean_tags)


# Exercise 3: Group transactions by type and compute total per type.

# Solution:
transactions = [
    {"type": "income",  "amount": 2000, "desc": "Salary"},
    {"type": "expense", "amount": 500,  "desc": "Rent"},
    {"type": "income",  "amount": 1500, "desc": "Freelance"},
    {"type": "expense", "amount": 300,  "desc": "Groceries"},
    {"type": "expense", "amount": 150,  "desc": "Utilities"},
]
by_type = defaultdict(list)
for t in transactions:
    by_type[t["type"]].append(t["amount"])

for t_type, amounts in by_type.items():
    print(f"{t_type.capitalize()}: total=${sum(amounts)}, count={len(amounts)}")


# Exercise 4: Build a lookup dict from a list of user records for O(1) access.

# Solution:
users = [
    {"id": 1, "name": "Alice"},
    {"id": 2, "name": "Bob"},
    {"id": 3, "name": "Charlie"},
]
users_by_id = {u["id"]: u for u in users}
print(users_by_id.get(2))   # {"id": 2, "name": "Bob"}
print(users_by_id.get(99))  # None


# Exercise 5: Find customers who bought both Product A and Product B.

# Solution:
product_a_buyers = {"alice", "bob", "charlie", "diana"}
product_b_buyers = {"bob", "diana", "eve", "frank"}
both = product_a_buyers & product_b_buyers
print("Bought both:", both)
