<!-- nav -->
[← Day 85](../Day85/lesson.md) | [🏠 Home](../../) | [Day 87 →](../Day87/lesson.md)

---
<!-- nav -->

# Day 86 – Project Scaffold & Database Schema

## Learning Objectives
- Set up a clean project directory structure
- Create the database schema and seed data
- Write a working "hello world" entry point

---

## Recommended Structure

```
expense_tracker/
├── app.py           ← entry point / CLI
├── db.py            ← all database code
├── logic.py         ← business logic (pure functions)
├── reports.py       ← report generation
├── requirements.txt
└── README.md
```

---

## Schema Design (Expense Tracker Example)

```sql
CREATE TABLE IF NOT EXISTS categories (
    id   INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL
);

CREATE TABLE IF NOT EXISTS expenses (
    id          INTEGER PRIMARY KEY AUTOINCREMENT,
    date        TEXT    NOT NULL,
    description TEXT    NOT NULL,
    amount      REAL    NOT NULL CHECK(amount > 0),
    category_id INTEGER NOT NULL REFERENCES categories(id)
);
```

---

## `db.py` Template

```python
import sqlite3
from pathlib import Path

DB_PATH = Path("expenses.db")

def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_conn() as conn:
        conn.executescript("""
            CREATE TABLE IF NOT EXISTS categories ( ... );
            CREATE TABLE IF NOT EXISTS expenses ( ... );
        """)
        conn.commit()

def seed_categories():
    cats = ["Food", "Transport", "Housing", "Entertainment", "Health", "Other"]
    with get_conn() as conn:
        conn.executemany(
            "INSERT OR IGNORE INTO categories (name) VALUES (?)",
            [(c,) for c in cats]
        )
        conn.commit()
```

---

## Entry Point

```python
# app.py
import db

def main():
    db.init_db()
    db.seed_categories()
    print("Expense Tracker v1.0")
    # ... rest of CLI

if __name__ == "__main__":
    main()
```

---

## Key Takeaways
- Scaffold everything before writing logic — empty modules are fine
- Seed data in a separate function that uses `INSERT OR IGNORE` so it's idempotent
- Run `python app.py` to verify the scaffold works before adding features

---

## Exercises
See `exercises.py`

---

<!-- nav -->
[📝 Exercises](https://github.com/nikunjjakhotia/Python-in-100-Days-course-hub/blob/main/Week13/Day86/exercises.py) | [🏠 Home](/Python-in-100-Days-course-hub/) | [← Day 85](../Day85/lesson.md) | [Day 87 →](../Day87/lesson.md)
<!-- nav -->
