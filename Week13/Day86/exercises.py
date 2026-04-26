# Day 86 – Project Scaffold & Database Schema
# Demonstrates a complete scaffold for an Expense Tracker capstone.

import sqlite3, os
from pathlib import Path
from datetime import date

DB_PATH = Path("capstone_demo.db")


# ─── db.py equivalent ────────────────────────────────────────────────────────

def get_conn():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_conn() as conn:
        conn.executescript("""
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
        """)
        conn.commit()

def seed_categories():
    cats = ["Food", "Transport", "Housing", "Entertainment", "Health", "Other"]
    with get_conn() as conn:
        conn.executemany(
            "INSERT OR IGNORE INTO categories (name) VALUES (?)", [(c,) for c in cats]
        )
        conn.commit()

def list_categories():
    with get_conn() as conn:
        return [dict(r) for r in conn.execute("SELECT * FROM categories ORDER BY name")]

def add_expense(date_str, description, amount, category_id):
    with get_conn() as conn:
        cur = conn.execute(
            "INSERT INTO expenses (date, description, amount, category_id) VALUES (?,?,?,?)",
            (date_str, description, amount, category_id)
        )
        conn.commit()
        return cur.lastrowid


# ─── Exercise: run the scaffold and verify it works ───────────────────────────

print("Initialising database…")
init_db()
seed_categories()

cats = list_categories()
print(f"Seeded {len(cats)} categories: {[c['name'] for c in cats]}")

# Add a sample expense
eid = add_expense(str(date.today()), "Coffee", 3.50, 1)
print(f"Added expense id={eid}")

# Verify
with get_conn() as conn:
    row = conn.execute("SELECT * FROM expenses WHERE id=?", (eid,)).fetchone()
    print("Stored expense:", dict(row))

# Clean up
DB_PATH.unlink(missing_ok=True)
print("Demo DB cleaned up.")
