# Day 88 – Core Feature Implementation — Part 2 (Update, Delete, Report)

import sqlite3
from pathlib import Path
from datetime import date

DB_PATH = Path("capstone88.db")


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
            INSERT OR IGNORE INTO categories (id, name) VALUES
                (1,'Food'),(2,'Transport'),(3,'Other');
            INSERT OR IGNORE INTO expenses (date, description, amount, category_id) VALUES
                ('2026-01-10','Coffee',3.50,1),
                ('2026-01-12','Bus',2.00,2),
                ('2026-01-20','Lunch',12.50,1),
                ('2026-02-05','Taxi',18.00,2);
        """)
        conn.commit()


def delete_expense(expense_id):
    with get_conn() as conn:
        conn.execute("DELETE FROM expenses WHERE id=?", (expense_id,))
        conn.commit()
        return conn.total_changes

def monthly_summary(year, month):
    with get_conn() as conn:
        rows = conn.execute("""
            SELECT c.name AS category, SUM(e.amount) AS total
            FROM expenses e JOIN categories c ON e.category_id = c.id
            WHERE strftime('%Y', e.date) = ? AND strftime('%m', e.date) = ?
            GROUP BY c.name ORDER BY total DESC
        """, (str(year), f"{month:02d}")).fetchall()
        return [dict(r) for r in rows]


# ─── Exercises ────────────────────────────────────────────────────────────────

init_db()

# Exercise 1: Delete an existing expense and confirm it's gone.
changed = delete_expense(1)
print("Deleted expense 1, rows changed:", changed)
with get_conn() as conn:
    remaining = conn.execute("SELECT COUNT(*) FROM expenses").fetchone()[0]
    print("Remaining expenses:", remaining)

# Exercise 2: Attempt to delete a non-existent expense.
changed = delete_expense(9999)
print("Delete non-existent, rows changed:", changed)

# Exercise 3: Get January 2026 monthly summary.
print("\nJanuary 2026 summary:")
for row in monthly_summary(2026, 1):
    print(f"  {row['category']:<15} ${row['total']:.2f}")

# Exercise 4: Get February 2026 summary.
print("\nFebruary 2026 summary:")
for row in monthly_summary(2026, 2):
    print(f"  {row['category']:<15} ${row['total']:.2f}")

# Exercise 5: Get a month with no data — should return empty list.
result = monthly_summary(2026, 6)
print("\nJune 2026 summary (should be empty):", result)

DB_PATH.unlink(missing_ok=True)
