<!-- nav -->
[← Day 69](../Day69/lesson.md) | [🏠 Home](../../) | [Day 71 →](../../Week11/Day71/lesson.md)

---
<!-- nav -->

# Day 70 – Project: Flask Task Manager

## What You're Building
A full-stack Flask web app where users can create, complete, and delete tasks — data persists in SQLite.

---

## Learning Objectives
- Combine routes, templates, forms, and database from Days 64–69
- Follow the MVC-lite pattern (routes + templates + db helpers)
- Deploy locally and test the full flow in a browser

---

## Project Structure

```
task_manager/
├── app.py
├── db.py
├── templates/
│   ├── base.html
│   └── index.html
└── static/
    └── style.css
```

---

## Routes

| Method | URL | Action |
|--------|-----|--------|
| GET | `/` | Show all tasks |
| POST | `/tasks` | Create task |
| POST | `/tasks/<id>/complete` | Mark done |
| POST | `/tasks/<id>/delete` | Delete task |

---

## `db.py` — Database Layer

```python
import sqlite3

DB = "tasks.db"

def get_conn():
    conn = sqlite3.connect(DB)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_conn() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id    INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                done  INTEGER NOT NULL DEFAULT 0
            )
        """)
        conn.commit()
```

---

## `app.py` Skeleton

```python
from flask import Flask, render_template, request, redirect, url_for
import db

app = Flask(__name__)
db.init_db()

@app.route("/")
def index():
    with db.get_conn() as conn:
        tasks = conn.execute("SELECT * FROM tasks ORDER BY id").fetchall()
    return render_template("index.html", tasks=tasks)

@app.route("/tasks", methods=["POST"])
def create_task():
    title = request.form.get("title", "").strip()
    if title:
        with db.get_conn() as conn:
            conn.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
            conn.commit()
    return redirect(url_for("index"))
```

---

## Stretch Goals
- Add CSS styling with a clean card layout
- Add due-date field and highlight overdue tasks in red
- Add a "Clear completed" bulk delete button

---

## Exercises
See `exercises.py`

---

<!-- nav -->
[📝 Exercises](https://github.com/nikunjjakhotia/Python-in-100-Days-course-hub/blob/main/Week10/Day70/exercises.py) | [← Day 69](../Day69/lesson.md) | [Day 71 →](../../Week11/Day71/lesson.md)
<!-- nav -->
