# Day 68 – SQLite with Flask

import sqlite3, os
from flask import Flask, jsonify, request, g

app     = Flask(__name__)
DB_PATH = "day68.db"


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
        db = get_db()
        db.executescript("""
            CREATE TABLE IF NOT EXISTS notes (
                id      INTEGER PRIMARY KEY AUTOINCREMENT,
                title   TEXT NOT NULL,
                content TEXT NOT NULL DEFAULT ''
            );
            INSERT OR IGNORE INTO notes (id, title, content)
            VALUES (1, 'First Note', 'Hello from SQLite!');
        """)
        db.commit()


# Exercise 1: GET /notes — return all notes as JSON.
@app.route("/notes")
def list_notes():
    rows = get_db().execute("SELECT * FROM notes ORDER BY id").fetchall()
    return jsonify([dict(r) for r in rows])


# Exercise 2: GET /notes/<id> — return one note or 404.
@app.route("/notes/<int:note_id>")
def get_note(note_id):
    row = get_db().execute("SELECT * FROM notes WHERE id=?", (note_id,)).fetchone()
    if row is None:
        return jsonify({"error": "Not found"}), 404
    return jsonify(dict(row))


# Exercise 3: POST /notes — create a new note from JSON body.
@app.route("/notes", methods=["POST"])
def create_note():
    data = request.get_json()
    if not data or "title" not in data:
        return jsonify({"error": "title required"}), 400
    db = get_db()
    cur = db.execute(
        "INSERT INTO notes (title, content) VALUES (?, ?)",
        (data["title"], data.get("content", ""))
    )
    db.commit()
    return jsonify({"id": cur.lastrowid}), 201


# Exercise 4: DELETE /notes/<id> — remove note.
@app.route("/notes/<int:note_id>", methods=["DELETE"])
def delete_note(note_id):
    db = get_db()
    db.execute("DELETE FROM notes WHERE id=?", (note_id,))
    db.commit()
    return "", 204


# ─── Test ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    init_db()
    client = app.test_client()

    print(client.get("/notes").get_json())
    r = client.post("/notes", json={"title": "Day 68", "content": "Flask + SQLite"})
    print("Created:", r.get_json())
    print(client.get("/notes").get_json())

    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)

    app.run(debug=True)
