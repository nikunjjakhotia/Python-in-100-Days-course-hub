<!-- nav -->
[← Day 56](../../Week08/Day56/lesson.md) | [🏠 Home](../../) | [Day 58 →](../Day58/lesson.md)

---
<!-- nav -->

# Day 57 – Intro to SQL & SQLite

## Learning Objectives
- Understand what a relational database is
- Know the core SQL keywords
- Connect to a SQLite database in Python

---

## What Is a Relational Database?

A relational database stores data in **tables** (like spreadsheets) with rows and columns. Tables link to each other via **foreign keys**.

| id | name  | email            |
|----|-------|------------------|
| 1  | Alice | alice@example.com|
| 2  | Bob   | bob@example.com  |

---

## Why SQLite?

SQLite is a **file-based** database — no server to install. Python includes it via the `sqlite3` module. Perfect for apps, prototypes, and small-to-medium datasets.

---

## Core SQL Keywords

| Keyword | Purpose |
|---------|---------|
| `CREATE TABLE` | Define a new table |
| `INSERT INTO` | Add rows |
| `SELECT` | Read rows |
| `WHERE` | Filter rows |
| `UPDATE` | Modify rows |
| `DELETE` | Remove rows |
| `DROP TABLE` | Delete a table |

---

## Connecting with Python

```python
import sqlite3

# Open (or create) a database file
conn = sqlite3.connect("myapp.db")
cursor = conn.cursor()

# Always close when done
conn.close()
```

Use a context manager to auto-close:
```python
with sqlite3.connect("myapp.db") as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT sqlite_version()")
    print(cursor.fetchone())
```

---

## Creating a Table

```python
with sqlite3.connect("myapp.db") as conn:
    conn.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id    INTEGER PRIMARY KEY AUTOINCREMENT,
            name  TEXT    NOT NULL,
            email TEXT    UNIQUE NOT NULL
        )
    """)
    conn.commit()
```

---

## Key Takeaways
- SQLite stores everything in a single `.db` file — no server needed
- `conn.cursor()` runs SQL; `conn.commit()` saves changes
- Always use `IF NOT EXISTS` so re-running your script doesn't crash

---

## Exercises
See `exercises.py`

---

<!-- nav -->
[📝 Exercises](https://github.com/nikunjjakhotia/Python-in-100-Days-course-hub/blob/main/Week09/Day57/exercises.py) | [← Day 56](../../Week08/Day56/lesson.md) | [Day 58 →](../Day58/lesson.md)
<!-- nav -->
