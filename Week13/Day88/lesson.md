<!-- nav -->
[← Day 87](../Day87/lesson.md) | [🏠 Home](../../) | [Day 89 →](../Day89/lesson.md)

---
<!-- nav -->

# Day 88 – Core Feature Implementation — Part 2

## Learning Objectives
- Build Update, Delete, and Report operations
- Generate a summary report using groupby-style aggregation
- Connect all features into an interactive CLI menu

---

## Feature 3 — Delete an Expense

```python
# db.py
def delete_expense(expense_id):
    with get_conn() as conn:
        conn.execute("DELETE FROM expenses WHERE id = ?", (expense_id,))
        conn.commit()
        return conn.total_changes   # 1 if deleted, 0 if not found
```

---

## Feature 4 — Monthly Summary Report

```python
# reports.py
def monthly_summary(year, month):
    import sqlite3
    from db import get_conn

    with get_conn() as conn:
        rows = conn.execute("""
            SELECT c.name AS category, SUM(e.amount) AS total
            FROM expenses e
            JOIN categories c ON e.category_id = c.id
            WHERE strftime('%Y', e.date) = ?
              AND strftime('%m', e.date) = ?
            GROUP BY c.name
            ORDER BY total DESC
        """, (str(year), f"{month:02d}")).fetchall()
        return [dict(r) for r in rows]
```

---

## CLI Menu — Connecting Everything

```python
# app.py
MENU = """
1. List expenses
2. Add expense
3. Delete expense
4. Monthly summary
5. Quit
"""

def run():
    while True:
        print(MENU)
        choice = input("> ").strip()
        if choice == "1":
            show_expenses()
        elif choice == "2":
            add_expense_prompt()
        elif choice == "3":
            delete_expense_prompt()
        elif choice == "4":
            monthly_report_prompt()
        elif choice == "5":
            break
```

---

## Key Takeaways
- `conn.total_changes` tells you whether a DELETE actually matched any row
- SQL aggregation (`GROUP BY + SUM`) is faster and cleaner than aggregating in Python
- The menu loop is the final glue — build it last, after all features work in isolation

---

## Exercises
See `exercises.py`

---

<!-- nav -->
[📝 Exercises](https://github.com/nikunjjakhotia/Python-in-100-Days-course-hub/blob/main/Week13/Day88/exercises.py) | [🏠 Home](/Python-in-100-Days-course-hub/) | [← Day 87](../Day87/lesson.md) | [Day 89 →](../Day89/lesson.md)
<!-- nav -->
