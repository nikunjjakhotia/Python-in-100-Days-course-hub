<!-- assignments-nav -->
[🏠 Home](../../) | [📚 Week 10 Lessons — Flask Web Development](../../Week10/)

---
<!-- assignments-nav -->

# Week 10 Assignment — Flask Task Manager

**Days 64–70 · Topics: Routes, URL Parameters, Jinja2 Templates, Forms, SQLite + Flask, REST API**

Build a full-stack web app where users can add, view, complete, and delete tasks — served through Flask with Jinja2 templates and a SQLite backend.

---

## 🎯 What You'll Build

A working web app you can open in any browser, backed by a real database, with a REST API endpoint alongside the HTML interface.

---

## 📋 Requirements

1. **Routes:** `GET /` to list all tasks, `POST /add` to create a task, `POST /done/<id>` to toggle completion, `POST /delete/<id>` to remove a task.
2. **Templates:** a `base.html` layout (nav bar + flash message area) extended by `tasks.html` that renders the task list and the add-task form.
3. **Server-side validation:** reject empty task titles and titles longer than 120 characters — display a flash message and do not save.
4. **SQLite persistence:** store tasks in `tasks.db` with columns `id`, `title`, `done` (BOOLEAN), `created_at` — tasks must survive a server restart.
5. **Styling:** apply basic CSS (inline or a linked `static/style.css`) so the page is readable — at minimum: a heading, a list, and styled buttons.
6. **REST endpoint:** `GET /api/tasks` returns all tasks as JSON `[{"id": 1, "title": "...", "done": false}, ...]` with status `200`; `GET /api/tasks/<id>` returns one task or `404`.
7. **PRG pattern:** after every `POST` route, redirect to `GET /` — never render a template directly from a POST handler.
8. Run the app with `debug=False` when sharing the screenshot — show it works without the debugger.

---

## 💡 Hints

- `flask.flash("message", "category")` stores a message; display it in `base.html` with `get_flashed_messages(with_categories=True)`.
- `flask.jsonify(tasks)` converts a list of dicts to a JSON response automatically.
- Initialize the database on startup: `with app.app_context(): db.init_db()`.
- `<form method="POST" action="/done/{{ task.id }}"><button>Done</button></form>` — HTML forms only support GET and POST, not DELETE.

---

## 📤 How to Submit

1. Save your solution as `Week10_assignment.py` (plus `templates/` and `static/`) inside this folder.
2. Start the server, add 3 tasks, mark one done, delete one, and confirm `/api/tasks` returns correct JSON.
3. Share a screenshot of the running app in the browser on LinkedIn with **#Python100Days** and tag [@nikunjjakhotia](https://www.linkedin.com/in/nikunjjakhotia/).

---

## ✅ Marking Criteria

| Criterion | Marks |
|-----------|-------|
| All 4 routes functional with correct HTTP methods | /10 |
| Jinja2 `base.html` + `tasks.html` template inheritance | /10 |
| Server-side validation with flash messages | /10 |
| SQLite persistence across server restarts | /10 |
| `/api/tasks` JSON endpoint returns correct data + status codes | /10 |
| **Total** | **/50** |
