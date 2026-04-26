# Day 70 – Project: Flask Task Manager
# Full-stack Flask + SQLite task manager.
# Run: python exercises.py  → http://127.0.0.1:5000

import sqlite3, os
from flask import Flask, render_template_string, request, redirect, url_for, g

app     = Flask(__name__)
DB_PATH = "tasks.db"

# ─── Database helpers ─────────────────────────────────────────────────────────

def get_db():
    if "db" not in g:
        g.db = sqlite3.connect(DB_PATH)
        g.db.row_factory = sqlite3.Row
    return g.db

@app.teardown_appcontext
def close_db(exc):
    db = g.pop("db", None)
    if db is not None:
        db.close()

def init_db():
    with app.app_context():
        get_db().executescript("""
            CREATE TABLE IF NOT EXISTS tasks (
                id    INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                done  INTEGER NOT NULL DEFAULT 0
            );
        """)
        get_db().commit()

# ─── Templates (inline for portability) ──────────────────────────────────────

INDEX_HTML = """
<!DOCTYPE html><html><head>
<title>Task Manager</title>
<style>
  body { font-family: sans-serif; max-width: 600px; margin: 40px auto; }
  li.done { text-decoration: line-through; color: #aaa; }
  form.inline { display: inline; }
</style>
</head><body>
<h1>Task Manager</h1>
<form method="POST" action="/tasks">
  <input name="title" placeholder="New task..." required style="width:70%">
  <button type="submit">Add</button>
</form>
<ul>
{% for t in tasks %}
  <li class="{{ 'done' if t.done else '' }}">
    {{ t.title }}
    {% if not t.done %}
    <form class="inline" method="POST" action="/tasks/{{ t.id }}/complete">
      <button>✓</button>
    </form>
    {% endif %}
    <form class="inline" method="POST" action="/tasks/{{ t.id }}/delete">
      <button>✗</button>
    </form>
  </li>
{% endfor %}
</ul>
</body></html>
"""

# ─── Routes ───────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    tasks = get_db().execute("SELECT * FROM tasks ORDER BY id").fetchall()
    return render_template_string(INDEX_HTML, tasks=tasks)

@app.route("/tasks", methods=["POST"])
def create_task():
    title = request.form.get("title", "").strip()
    if title:
        db = get_db()
        db.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
        db.commit()
    return redirect(url_for("index"))

@app.route("/tasks/<int:task_id>/complete", methods=["POST"])
def complete_task(task_id):
    db = get_db()
    db.execute("UPDATE tasks SET done = 1 WHERE id = ?", (task_id,))
    db.commit()
    return redirect(url_for("index"))

@app.route("/tasks/<int:task_id>/delete", methods=["POST"])
def delete_task(task_id):
    db = get_db()
    db.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    db.commit()
    return redirect(url_for("index"))


if __name__ == "__main__":
    init_db()
    app.run(debug=True)
