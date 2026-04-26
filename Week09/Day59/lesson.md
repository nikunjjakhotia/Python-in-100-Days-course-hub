# Day 59 – SELECT Queries & Filtering

## Learning Objectives
- Write SELECT queries with WHERE, ORDER BY, and LIMIT
- Use aggregate functions: COUNT, SUM, AVG, MIN, MAX
- Fetch results as dicts using `row_factory`

---

## Basic SELECT

```python
import sqlite3

with sqlite3.connect("shop.db") as conn:
    rows = conn.execute("SELECT * FROM products").fetchall()
    for row in rows:
        print(row)   # tuple: (id, name, price, category)
```

---

## WHERE, ORDER BY, LIMIT

```python
# Filter
rows = conn.execute(
    "SELECT name, price FROM products WHERE price < ?", (10.0,)
).fetchall()

# Sort descending
rows = conn.execute(
    "SELECT * FROM products ORDER BY price DESC"
).fetchall()

# Limit
rows = conn.execute(
    "SELECT * FROM products ORDER BY price DESC LIMIT 3"
).fetchall()
```

---

## Aggregate Functions

```python
row = conn.execute("SELECT COUNT(*), AVG(price), MAX(price) FROM products").fetchone()
count, avg_price, max_price = row
print(f"Products: {count}, Avg: ${avg_price:.2f}, Max: ${max_price:.2f}")
```

---

## `fetchone` vs `fetchall` vs `fetchmany`

```python
cur = conn.execute("SELECT * FROM products")
first  = cur.fetchone()              # one tuple or None
three  = cur.fetchmany(3)            # list of up to 3 tuples
rest   = cur.fetchall()              # remaining rows
```

---

## Row Factory — Results as Dicts

```python
conn.row_factory = sqlite3.Row   # set before querying

rows = conn.execute("SELECT * FROM products").fetchall()
for row in rows:
    print(dict(row))             # {'id': 1, 'name': 'Widget', ...}
```

---

## Key Takeaways
- Always use `?` in WHERE clauses with parameterised values
- `sqlite3.Row` lets you access columns by name: `row["price"]`
- Aggregates (`COUNT`, `AVG`, `SUM`) let you summarise data without Python loops

---

## Exercises
See `exercises.py`
