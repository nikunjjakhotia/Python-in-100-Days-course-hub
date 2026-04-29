<!-- assignments-nav -->
[🏠 Home](../../) | [📚 Week 10 Lessons — Flask Web Development](../../Week10/)

---
<!-- assignments-nav -->

# Week 10 Assignment: Build a Flask Task Manager

**Days 64–70 · Topics: Routes, URL Params, Jinja2 Templates, Forms, SQLite + Flask, REST API**

Using the Flask skills from Days 64–70, build a full-stack web app where users can add, view, and delete tasks — backed by SQLite and served through Jinja2 templates.

## What to Build
- Three routes: `GET /` to list tasks, `POST /add` to create a task, `POST /delete/<id>` to remove one
- A `base.html` layout with a nav bar, extended by a `tasks.html` page that renders the task list
- Server-side form validation: reject empty task titles and display a flash message
- SQLite persistence via `sqlite3` — no task is lost when the server restarts
- A `/api/tasks` endpoint that returns all tasks as JSON with correct HTTP status codes
