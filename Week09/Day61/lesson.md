<!-- nav -->
[← Day 60](../Day60/lesson.md) | [🏠 Home](../../) | [Day 62 →](../Day62/lesson.md)

---
<!-- nav -->

# Day 61 – Python `sqlite3` Module Deep Dive

## Learning Objectives
- Use `row_factory` to get dict-like rows
- Work with multiple tables and JOIN
- Use `executescript` for schema migrations

---

## Row Factory

```python
import sqlite3

def dict_factory(cursor, row):
    return {col[0]: row[i] for i, col in enumerate(cursor.description)}

conn = sqlite3.connect("app.db")
conn.row_factory = dict_factory   # or sqlite3.Row (built-in)
```

With `sqlite3.Row`:
```python
conn.row_factory = sqlite3.Row
row = conn.execute("SELECT * FROM users WHERE id = ?", (1,)).fetchone()
print(row["name"], row["email"])
print(dict(row))
```

---

## Multiple Tables & JOIN

```python
conn.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id         INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id    INTEGER NOT NULL REFERENCES users(id),
        product    TEXT,
        amount     REAL
    )
""")

rows = conn.execute("""
    SELECT users.name, orders.product, orders.amount
    FROM orders
    JOIN users ON orders.user_id = users.id
    WHERE orders.amount > ?
""", (20.0,)).fetchall()
```

---

## `executescript` for Migrations

```python
conn.executescript("""
    CREATE TABLE IF NOT EXISTS categories (
        id   INTEGER PRIMARY KEY,
        name TEXT UNIQUE
    );
    INSERT OR IGNORE INTO categories (name) VALUES ('books'),('tech'),('food');
""")
```

---

## Checking Whether a Table Exists

```python
exists = conn.execute(
    "SELECT name FROM sqlite_master WHERE type='table' AND name=?",
    ("users",)
).fetchone()
print("Table exists:", exists is not None)
```

---

## Key Takeaways
- `sqlite3.Row` is the easiest way to get column-name access
- `JOIN` combines data from two tables on a shared key
- `executescript` runs multiple SQL statements at once — great for schema setup

---

## Exercises
See `exercises.py`

---

<!-- nav -->
[📝 Exercises](exercises.py) | [← Day 60](../Day60/lesson.md) | [Day 62 →](../Day62/lesson.md)
<!-- nav -->
