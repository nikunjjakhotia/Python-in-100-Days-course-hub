# Day 87 – Core Feature Implementation — Part 1

## Learning Objectives
- Build the Create and Read operations of the capstone
- Write thin controller functions that delegate to the data layer
- Manually test each feature before moving on

---

## Feature 1 — Add an Expense

```python
# logic.py
from datetime import date as _date

def validate_expense(description, amount, category_id):
    errors = []
    if not description.strip():
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
```

```python
# db.py
def add_expense(date, description, amount, category_id):
    with get_conn() as conn:
        cur = conn.execute(
            "INSERT INTO expenses (date, description, amount, category_id) VALUES (?, ?, ?, ?)",
            (date, description.strip(), float(amount), category_id)
        )
        conn.commit()
        return cur.lastrowid
```

---

## Feature 2 — List Expenses

```python
# db.py
def list_expenses(limit=50):
    with get_conn() as conn:
        rows = conn.execute("""
            SELECT e.id, e.date, e.description, e.amount, c.name AS category
            FROM expenses e
            JOIN categories c ON e.category_id = c.id
            ORDER BY e.date DESC
            LIMIT ?
        """, (limit,)).fetchall()
        return [dict(r) for r in rows]
```

---

## Manual Testing Checklist

Before moving to Feature 3, verify:
- [ ] Can add an expense and it appears in list
- [ ] Empty description is rejected
- [ ] Negative amount is rejected
- [ ] Expenses appear in newest-first order

---

## Key Takeaways
- Write validation in `logic.py` (no DB imports) — it's easy to unit-test
- Keep DB functions thin: just SQL + commit, no business rules
- Test manually after every feature — don't batch features and test at the end

---

## Exercises
See `exercises.py`
