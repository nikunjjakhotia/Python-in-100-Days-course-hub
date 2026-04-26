# Day 60 – UPDATE, DELETE & Transactions

## Learning Objectives
- Update existing rows with UPDATE … SET … WHERE
- Delete rows with DELETE … WHERE
- Understand transactions and rollbacks

---

## UPDATE

```python
import sqlite3

with sqlite3.connect("shop.db") as conn:
    conn.execute(
        "UPDATE products SET price = ? WHERE name = ?",
        (12.99, "Widget")
    )
    conn.commit()
    print("Rows changed:", conn.total_changes)
```

---

## DELETE

```python
with sqlite3.connect("shop.db") as conn:
    conn.execute("DELETE FROM products WHERE price < ?", (1.0,))
    conn.commit()
```

---

## Transactions

SQLite wraps every write in a transaction. Changes are invisible to other connections until `commit()`. If something fails, call `rollback()`:

```python
conn = sqlite3.connect("shop.db")
try:
    conn.execute("INSERT INTO products (name, price) VALUES (?, ?)", ("X", 5.0))
    conn.execute("UPDATE products SET price = ? WHERE id = ?", (0.0, 1))
    conn.commit()
except Exception as e:
    conn.rollback()
    print("Rolled back:", e)
finally:
    conn.close()
```

Using `with sqlite3.connect(...) as conn:` commits on exit, rolls back on exception automatically.

---

## DROP TABLE

```python
conn.execute("DROP TABLE IF EXISTS old_table")
conn.commit()
```

---

## Key Takeaways
- Always include a `WHERE` in UPDATE and DELETE — without it you affect every row
- `conn.total_changes` tells you how many rows were affected
- The `with` context manager handles commit/rollback automatically

---

## Exercises
See `exercises.py`
