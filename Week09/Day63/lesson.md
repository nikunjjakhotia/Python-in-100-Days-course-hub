<!-- nav -->
[← Day 62](../Day62/lesson.md) | [🏠 Home](../../) | [Day 64 →](../../Week10/Day64/lesson.md)

---
<!-- nav -->

# Day 63 – Project: To-Do List Database App

## What You're Building
A command-line to-do list backed by SQLite — tasks persist between runs.

---

## Learning Objectives
- Apply the full CRUD pattern from Day 62
- Build an interactive CLI menu
- Use `datetime` to timestamp tasks

---

## Project Spec

```
Todo App
─────────────────────────────
1. List all tasks
2. Add task
3. Complete task
4. Delete task
5. Quit
> 2
Task: Buy groceries
Added task #3.
> 1

ID  Done  Created      Task
──────────────────────────────────
 1   ✓   2026-04-20   Write lesson notes
 2        2026-04-21   Review pull requests
 3        2026-04-26   Buy groceries
```

---

## Schema

```sql
CREATE TABLE IF NOT EXISTS tasks (
    id         INTEGER PRIMARY KEY AUTOINCREMENT,
    title      TEXT    NOT NULL,
    done       INTEGER NOT NULL DEFAULT 0,
    created_at TEXT    NOT NULL
);
```

---

## Implementation Guide

```python
import sqlite3
from datetime import datetime

DB_PATH = "todo.db"

def setup(conn): ...
def add_task(conn, title): ...
def list_tasks(conn): ...
def complete_task(conn, task_id): ...
def delete_task(conn, task_id): ...

def main():
    with sqlite3.connect(DB_PATH) as conn:
        conn.row_factory = sqlite3.Row
        setup(conn)
        while True:
            choice = input("> ").strip()
            ...
```

---

## Stretch Goals
- Add due-date support with overdue highlighting
- Filter by status: `list pending`, `list done`
- Export to CSV with `import csv`

---

## Exercises
See `exercises.py`

---

## 📝 Week 9 Assignment

You've completed Week 9! Time to put it all together.

**[→ Complete the Week 9 Assignment](../../Assignments/Week09/)**

---

<!-- nav -->
[📝 Exercises](https://github.com/nikunjjakhotia/Python-in-100-Days-course-hub/blob/main/Week09/Day63/exercises.py) | [🏠 Home](/Python-in-100-Days-course-hub/) | [← Day 62](../Day62/lesson.md) | [Day 64 →](../../Week10/Day64/lesson.md)
<!-- nav -->
