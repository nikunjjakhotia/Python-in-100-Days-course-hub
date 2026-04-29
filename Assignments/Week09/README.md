<!-- assignments-nav -->
[🏠 Home](../../) | [📚 Week 09 Lessons — SQLite & Databases](../../Week09/)

---
<!-- assignments-nav -->

# Week 9 Assignment — To-Do List Database App

**Days 57–63 · Topics: SQL Basics, INSERT/SELECT/UPDATE/DELETE, Transactions, CRUD, sqlite3**

Build a fully persistent CLI to-do list app backed by a SQLite database, with priorities, due dates, and CSV export.

---

## 🎯 What You'll Build

A CLI app where tasks survive between runs because they live in a real database — with filtering, bulk operations, and export.

---

## 📋 Requirements

1. Create a `todos.db` SQLite database with a `tasks` table: `id` (PK), `title` (NOT NULL), `priority` (1–3), `due_date` (TEXT, ISO format), `done` (BOOLEAN DEFAULT 0), `created_at` (TEXT).
2. Support **full CRUD** from a menu: add task, list all tasks, mark task as done, update title or due date, delete task.
3. Use **parameterised queries** throughout (`?` placeholders) — never format user input directly into SQL strings.
4. Implement **filtering**: list only pending tasks, list only high-priority (1) tasks, list tasks due today or earlier.
5. Use a **transaction** for a `bulk_add(tasks_list)` function that inserts multiple tasks at once and rolls back entirely if any one fails.
6. Use `sqlite3.Row` as the `row_factory` so columns are accessible by name (e.g. `row["title"]`).
7. Implement a `mark_all_done()` function with an `UPDATE` statement — confirm with the user before executing.
8. Export all tasks to `tasks.csv` using Python's `csv.DictWriter` with all table columns as headers.

---

## 💡 Hints

- `conn.row_factory = sqlite3.Row` — set this right after `sqlite3.connect()`.
- `datetime.date.today().isoformat()` gives the ISO date string `"YYYY-MM-DD"` for due dates.
- `conn.execute("BEGIN"); ...; conn.commit()` is the explicit transaction pattern.
- `WHERE done = 0 AND due_date <= date('now')` filters overdue tasks in SQL.

---

## 📤 How to Submit

1. Save your solution as `Week09_assignment.py` inside this folder.
2. Run it, add 5 tasks, mark 2 as done, filter by pending, then export to CSV.
3. Share a screenshot of the task list on LinkedIn with **#Python100Days** and tag [@nikunjjakhotia](https://www.linkedin.com/in/nikunjjakhotia/).

---

## ✅ Marking Criteria

| Criterion | Marks |
|-----------|-------|
| Database and table created with all required columns | /10 |
| Full CRUD operations work correctly | /15 |
| Parameterised queries used throughout (no f-string SQL) | /10 |
| Filtering by status, priority, and due date works | /10 |
| Bulk add transaction and CSV export work correctly | /5 |
| **Total** | **/50** |
