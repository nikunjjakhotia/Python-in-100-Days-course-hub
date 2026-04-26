# Day 89 – Testing with unittest

import unittest, sqlite3
from pathlib import Path


# ─── Code under test (inline for portability) ────────────────────────────────

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


def get_conn(db_path=":memory:"):
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def init_db(conn):
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS categories (
            id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT UNIQUE NOT NULL
        );
        CREATE TABLE IF NOT EXISTS expenses (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL, description TEXT NOT NULL,
            amount REAL NOT NULL, category_id INTEGER NOT NULL
        );
        INSERT OR IGNORE INTO categories (id, name) VALUES (1,'Food'),(2,'Transport');
    """)
    conn.commit()

def add_expense(conn, date_str, description, amount, category_id):
    cur = conn.execute(
        "INSERT INTO expenses (date, description, amount, category_id) VALUES (?,?,?,?)",
        (date_str, description, float(amount), category_id)
    )
    conn.commit()
    return cur.lastrowid

def list_expenses(conn):
    return [dict(r) for r in conn.execute("SELECT * FROM expenses ORDER BY id")]

def delete_expense(conn, eid):
    conn.execute("DELETE FROM expenses WHERE id=?", (eid,))
    conn.commit()
    return conn.total_changes


# ─── Tests ────────────────────────────────────────────────────────────────────

class TestValidation(unittest.TestCase):
    def test_valid_expense(self):
        self.assertEqual(validate_expense("Coffee", 3.50, 1), [])

    def test_empty_description(self):
        self.assertIn("Description is required.", validate_expense("", 3.50, 1))

    def test_negative_amount(self):
        self.assertIn("Amount must be positive.", validate_expense("X", -1.0, 1))

    def test_zero_amount(self):
        self.assertIn("Amount must be positive.", validate_expense("X", 0, 1))

    def test_non_numeric_amount(self):
        self.assertIn("Amount must be a number.", validate_expense("X", "abc", 1))

    def test_missing_category(self):
        self.assertIn("Category is required.", validate_expense("X", 5.0, None))


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.conn = get_conn(":memory:")
        init_db(self.conn)

    def tearDown(self):
        self.conn.close()

    def test_add_and_list(self):
        add_expense(self.conn, "2026-01-01", "Coffee", 3.50, 1)
        expenses = list_expenses(self.conn)
        self.assertEqual(len(expenses), 1)
        self.assertEqual(expenses[0]["description"], "Coffee")
        self.assertAlmostEqual(expenses[0]["amount"], 3.50)

    def test_delete_existing(self):
        eid = add_expense(self.conn, "2026-01-01", "Lunch", 12.0, 1)
        changed = delete_expense(self.conn, eid)
        self.assertEqual(changed, 1)
        self.assertEqual(list_expenses(self.conn), [])

    def test_delete_nonexistent(self):
        changed = delete_expense(self.conn, 9999)
        self.assertEqual(changed, 0)

    def test_multiple_expenses(self):
        for i in range(5):
            add_expense(self.conn, "2026-01-01", f"Item {i}", float(i + 1), 1)
        self.assertEqual(len(list_expenses(self.conn)), 5)


if __name__ == "__main__":
    unittest.main(verbosity=2)
