<!-- nav -->
[← Day 88](../Day88/lesson.md) | [🏠 Home](../../) | [Day 90 →](../Day90/lesson.md)

---
<!-- nav -->

# Day 89 – Testing with `unittest`

## Learning Objectives
- Write unit tests with the `unittest` module
- Test business logic in isolation from the database
- Use `setUp` / `tearDown` for an in-memory test database

---

## Why Test?

Tests catch regressions — bugs you accidentally reintroduce. They also make refactoring safe and document expected behaviour.

---

## Basic Test Structure

```python
import unittest

class TestValidation(unittest.TestCase):

    def test_valid_expense(self):
        errors = validate_expense("Coffee", 3.50, 1)
        self.assertEqual(errors, [])

    def test_empty_description(self):
        errors = validate_expense("", 3.50, 1)
        self.assertIn("Description is required.", errors)

    def test_negative_amount(self):
        errors = validate_expense("Coffee", -1.0, 1)
        self.assertIn("Amount must be positive.", errors)

if __name__ == "__main__":
    unittest.main()
```

---

## Testing with an In-Memory DB

```python
import sqlite3, unittest
import db   # your db module

class TestDB(unittest.TestCase):

    def setUp(self):
        # override DB_PATH to use in-memory database
        db.DB_PATH = ":memory:"
        db.init_db()
        db.seed_categories()

    def tearDown(self):
        # nothing to clean — in-memory DB disappears automatically
        pass

    def test_add_and_list(self):
        db.add_expense("2026-01-01", "Coffee", 3.50, 1)
        expenses = db.list_expenses()
        self.assertEqual(len(expenses), 1)
        self.assertEqual(expenses[0]["description"], "Coffee")

    def test_delete_nonexistent(self):
        changed = db.delete_expense(9999)
        self.assertEqual(changed, 0)
```

---

## Common Assertions

| Method | Checks |
|--------|--------|
| `assertEqual(a, b)` | `a == b` |
| `assertIn(x, seq)` | `x in seq` |
| `assertTrue(expr)` | expr is truthy |
| `assertRaises(Exc)` | context manager for exceptions |
| `assertAlmostEqual(a, b)` | floats within 7 decimal places |

---

## Key Takeaways
- Test business logic separately from the database — use an in-memory SQLite for DB tests
- `setUp` / `tearDown` run before/after every test method
- Run tests with `python -m unittest discover` from the project root

---

## Exercises
See `exercises.py`

---

<!-- nav -->
[📝 Exercises](https://github.com/nikunjjakhotia/Python-in-100-Days-course-hub/blob/main/Week13/Day89/exercises.py) | [← Day 88](../Day88/lesson.md) | [Day 90 →](../Day90/lesson.md)
<!-- nav -->
