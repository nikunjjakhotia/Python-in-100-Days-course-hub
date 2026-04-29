<!-- nav -->
[← Day 57](../Day57/lesson.md) | [🏠 Home](../../) | [Day 59 →](../Day59/lesson.md)

---
<!-- nav -->

# Day 58 – Creating Tables & Inserting Data

## Learning Objectives
- Design a table with appropriate data types and constraints
- Insert single and multiple rows
- Use parameterised queries to prevent SQL injection

---

## SQLite Data Types

| Python | SQLite |
|--------|--------|
| `int` | `INTEGER` |
| `float` | `REAL` |
| `str` | `TEXT` |
| `bytes` | `BLOB` |
| `None` | `NULL` |

---

## Table Constraints

```sql
CREATE TABLE products (
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    name     TEXT    NOT NULL,
    price    REAL    NOT NULL CHECK(price >= 0),
    category TEXT    DEFAULT 'general',
    UNIQUE(name)
);
```

---

## Inserting a Single Row

Always use `?` placeholders — **never** string-format user data into SQL:

```python
import sqlite3

with sqlite3.connect("shop.db") as conn:
    conn.execute(
        "INSERT INTO products (name, price, category) VALUES (?, ?, ?)",
        ("Widget", 9.99, "hardware")
    )
    conn.commit()
```

---

## Inserting Many Rows

```python
products = [
    ("Gadget",  14.99, "electronics"),
    ("Sprocket", 3.49, "hardware"),
    ("Doohickey", 7.00, "misc"),
]

with sqlite3.connect("shop.db") as conn:
    conn.executemany(
        "INSERT INTO products (name, price, category) VALUES (?, ?, ?)",
        products
    )
    conn.commit()
```

---

## Getting the Last Inserted ID

```python
with sqlite3.connect("shop.db") as conn:
    cur = conn.execute(
        "INSERT INTO products (name, price) VALUES (?, ?)",
        ("New Item", 5.00)
    )
    conn.commit()
    print("New row id:", cur.lastrowid)
```

---

## Key Takeaways
- Always use parameterised queries (`?` placeholders) — never f-string SQL
- `executemany()` is efficient for bulk inserts
- `cur.lastrowid` gives the auto-generated primary key of the last insert

---

## Exercises
See `exercises.py`

---

<!-- nav -->
[📝 Exercises](https://github.com/nikunjjakhotia/Python-in-100-Days-course-hub/blob/main/Week09/Day58/exercises.py) | [🏠 Home](/Python-in-100-Days-course-hub/) | [← Day 57](../Day57/lesson.md) | [Day 59 →](../Day59/lesson.md)
<!-- nav -->
