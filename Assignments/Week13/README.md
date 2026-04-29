<!-- assignments-nav -->
[🏠 Home](../../) | [📚 Week 13 Lessons — Capstone Project](../../Week13/)

---
<!-- assignments-nav -->

# Week 13 Assignment — Capstone: Personal Finance Tracker

**Days 85–91 · Topics: Architecture, Scaffolding, CRUD, Testing, Documentation, Code Review**

Design and build a full-stack personal finance tracker that integrates Flask, SQLite, and pandas — your largest Python project to date.

---

## 🎯 What You'll Build

A web app where a user can log income and expenses, view a category breakdown, and see a spending trend chart — all backed by a real database and covered by unit tests.

---

## 📋 Requirements

1. **Day 85 spec (submit before coding):** write a `spec.md` covering: problem statement, target user, 5 core features, a data model sketch (table names and columns), and your technology choices with justification.
2. **Database:** a `finance.db` SQLite database with at least two tables — `transactions` (id, type, amount, category, date, note) and `categories` (id, name, colour).
3. **Flask routes:** `GET /` dashboard, `POST /add` to create a transaction, `GET /history` to list all transactions with filtering by category and date range, `POST /delete/<id>` to remove one.
4. **pandas analysis:** on the dashboard, display total income, total expenses, net balance, and a per-category spending breakdown — computed from the database using pandas `read_sql_query`.
5. **Chart:** generate a monthly spending bar chart using matplotlib, save it to `static/chart.png`, and embed it in the dashboard template — regenerate it on every page load.
6. **Templates:** a `base.html` layout extended by at least `dashboard.html` and `history.html`; use Jinja2 filters for currency formatting.
7. **Tests:** at least **8 unit tests** in `test_finance.py` using `unittest` — include 2 tests that insert into an in-memory SQLite (`":memory:"`) and verify the result.
8. **README.md:** project title, problem description, features list, Quick Start steps (clone → install → run), project structure tree, and technologies used.

---

## 💡 Hints

- `pd.read_sql_query("SELECT ...", conn)` reads a query result directly into a DataFrame.
- `df.groupby("category")["amount"].sum()` gives per-category totals.
- `fig.savefig("static/chart.png")` inside the Flask route — call `plt.close(fig)` immediately after to avoid memory leaks.
- `unittest.TestCase.setUp` can create an in-memory DB and seed it before each test.

---

## 📤 How to Submit

1. Commit all files (`app.py`, `templates/`, `static/`, `test_finance.py`, `README.md`, `requirements.txt`) to this folder.
2. Run `python -m unittest test_finance.py` — all 8 tests must pass.
3. Share a screenshot of the running dashboard on LinkedIn with **#Python100Days** and tag [@nikunjjakhotia](https://www.linkedin.com/in/nikunjjakhotia/).

---

## ✅ Marking Criteria

| Criterion | Marks |
|-----------|-------|
| All Flask routes functional (dashboard, add, history, delete) | /15 |
| pandas analysis displayed correctly on dashboard | /10 |
| Monthly spending chart generated and embedded | /10 |
| 8 unit tests written and passing (including 2 DB tests) | /10 |
| README.md complete with Quick Start and project structure | /5 |
| **Total** | **/50** |

---

*If this course is helping you, please ⭐ [star the repo](https://github.com/nikunjjakhotia/Python-in-100-Days-course-hub) — it helps others find it!*
