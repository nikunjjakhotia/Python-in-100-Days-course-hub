# Day 87 – Core Feature Implementation — Part 1 (Create & Read)

import sqlite3, os
from pathlib import Path
from datetime import date

DB_PATH = Path("capstone87.db")


def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_conn() as conn:
        conn.executescript("""
            CREATE TABLE IF NOT EXISTS categories (
                id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT UNIQUE NOT NULL
            );
            CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                date TEXT NOT NULL, description TEXT NOT NULL,
                amount REAL NOT NULL CHECK(amount > 0),
                category_id INTEGER NOT NULL REFERENCES categories(id)
            );
            INSERT OR IGNORE INTO categories (name)
            VALUES ('Food'),('Transport'),('Housing'),('Other');
        """)
        conn.commit()


# ─── logic.py equivalent ─────────────────────────────────────────────────────

def validate_expense(description, amount, category_id):
    errors = []
    if not str(description).strip():
        errors.append("Description is required.")
    try:
        a = float(amount)
        if a <= 0:
            errors.append("Amount must be positive.")
    except (ValueError, TypeError):
        errors.append("Amount must be a number.")
    if not category_id:
        errors.append("Category is required.")
    return errors


# ─── db functions ─────────────────────────────────────────────────────────────

def add_expense(date_str, description, amount, category_id):
    errors = validate_expense(description, amount, category_id)
    if errors:
        return None, errors
    with get_conn() as conn:
        cur = conn.execute(
            "INSERT INTO expenses (date, description, amount, category_id) VALUES (?,?,?,?)",
            (date_str, description.strip(), float(amount), int(category_id))
        )
        conn.commit()
        return cur.lastrowid, []

def list_expenses():
    with get_conn() as conn:
        rows = conn.execute("""
            SELECT e.id, e.date, e.description, e.amount, c.name AS category
            FROM expenses e JOIN categories c ON e.category_id = c.id
            ORDER BY e.date DESC
        """).fetchall()
        return [dict(r) for r in rows]


# ─── Exercises ────────────────────────────────────────────────────────────────

init_db()

# Exercise 1: Add valid expenses and list them.
id1, err = add_expense(str(date.today()), "Groceries", 45.00, 1)
id2, err = add_expense(str(date.today()), "Bus pass",  30.00, 2)
print("Added ids:", id1, id2)
print("\nAll expenses:")
for e in list_expenses():
    print(f"  #{e['id']} {e['date']} {e['description']:<20} ${e['amount']:.2f} [{e['category']}]")

# Exercise 2: Try invalid inputs and check errors.
_, errors = add_expense(str(date.today()), "",   45.00, 1)
print("\nEmpty description errors:", errors)
_, errors = add_expense(str(date.today()), "X", -5.00, 1)
print("Negative amount errors:", errors)
_, errors = add_expense(str(date.today()), "Y",  "abc", 1)
print("Non-numeric amount errors:", errors)

DB_PATH.unlink(missing_ok=True)
