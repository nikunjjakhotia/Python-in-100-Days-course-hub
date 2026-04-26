# Day 68 – SQLite with Flask

## Learning Objectives
- Connect SQLite to a Flask app per request
- Use `g` and `teardown_appcontext` for connection management
- Build a basic data-driven route

---

## Per-Request Database Connections

Flask provides `g` — a request-scoped namespace. Store the connection there so it's created once per request and closed automatically:

```python
import sqlite3
from flask import Flask, g

app = Flask(__name__)
DB_PATH = "app.db"

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
```

---

## Using the Connection in a Route

```python
@app.route("/users")
def users():
    db   = get_db()
    rows = db.execute("SELECT * FROM users ORDER BY name").fetchall()
    return render_template("users.html", users=[dict(r) for r in rows])
```

---

## Initialising the Schema

```python
@app.cli.command("init-db")
def init_db():
    db = get_db()
    db.executescript("""
        CREATE TABLE IF NOT EXISTS users (
            id    INTEGER PRIMARY KEY AUTOINCREMENT,
            name  TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL
        );
    """)
    db.commit()
    print("Database initialised.")
```

Run: `flask init-db`

---

## Full CRUD Example (one route each)

```python
@app.route("/users/<int:uid>", methods=["GET"])
def get_user(uid):
    row = get_db().execute("SELECT * FROM users WHERE id=?", (uid,)).fetchone()
    if row is None:
        return "Not found", 404
    return dict(row)

@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    db   = get_db()
    db.execute("INSERT INTO users (name, email) VALUES (?, ?)", (data["name"], data["email"]))
    db.commit()
    return "Created", 201
```

---

## Key Takeaways
- `g` is request-scoped — never store per-user data in `app` globals
- `teardown_appcontext` reliably closes the connection after every request
- Use `flask <command>` CLI commands for one-off admin tasks like `init-db`

---

## Exercises
See `exercises.py`
