# Day 91 – Final Polish & Code Review

# Exercise 1: Run the self-review checklist against the functions below.
# Find and fix the issues.

# ── BEFORE (buggy / messy code) ──────────────────────────────────────────────

import sqlite3

def get_expenses_BUGGY(db_path, category=None):
    # BUG 1: no parameterised query — SQL injection risk
    # BUG 2: never closes the connection
    # BUG 3: returns raw tuples instead of dicts
    conn = sqlite3.connect(db_path)
    if category:
        sql = f"SELECT * FROM expenses WHERE category = '{category}'"  # DANGEROUS
    else:
        sql = "SELECT * FROM expenses"
    return conn.execute(sql).fetchall()


# ── AFTER (fixed) ─────────────────────────────────────────────────────────────

def get_expenses(db_path, category=None):
    """Return all expenses, optionally filtered by category name."""
    with sqlite3.connect(db_path) as conn:
        conn.row_factory = sqlite3.Row
        if category:
            rows = conn.execute(
                """SELECT e.*, c.name AS cat_name FROM expenses e
                   JOIN categories c ON e.category_id = c.id
                   WHERE c.name = ?""",
                (category,)
            ).fetchall()
        else:
            rows = conn.execute(
                """SELECT e.*, c.name AS cat_name FROM expenses e
                   JOIN categories c ON e.category_id = c.id"""
            ).fetchall()
        return [dict(r) for r in rows]

print("get_expenses uses parameterised queries: OK")


# Exercise 2: Write a helper function to format an expense for display,
# and show it eliminates repeated formatting code.

def format_expense(e: dict) -> str:
    return (f"#{e.get('id', '?'):<4} "
            f"{e.get('date','N/A'):<12} "
            f"{e.get('description',''):<25} "
            f"${e.get('amount', 0):.2f}")

sample_expenses = [
    {"id": 1, "date": "2026-01-10", "description": "Coffee",      "amount": 3.50},
    {"id": 2, "date": "2026-01-12", "description": "Bus pass",    "amount": 30.00},
    {"id": 3, "date": "2026-01-20", "description": "Grocery run", "amount": 62.40},
]

print("\nFormatted expenses:")
for e in sample_expenses:
    print(format_expense(e))


# Exercise 3: Verify edge-case handling — empty list should print "No expenses found."

def print_expenses(expenses):
    if not expenses:
        print("No expenses found.")
        return
    for e in expenses:
        print(format_expense(e))

print("\nEmpty list test:")
print_expenses([])

print("\nFull list test:")
print_expenses(sample_expenses)
