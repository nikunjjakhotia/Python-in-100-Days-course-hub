# Day 62 – Building a CRUD App

import sqlite3, os

DB = "contacts.db"


class ContactDB:
    def __init__(self, path=DB):
        self._conn = sqlite3.connect(path)
        self._conn.row_factory = sqlite3.Row
        self._setup()

    def _setup(self):
        self._conn.execute("""
            CREATE TABLE IF NOT EXISTS contacts (
                id    INTEGER PRIMARY KEY AUTOINCREMENT,
                name  TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL,
                phone TEXT
            )
        """)
        self._conn.commit()

    def add(self, name, email, phone=None):
        try:
            cur = self._conn.execute(
                "INSERT INTO contacts (name, email, phone) VALUES (?, ?, ?)",
                (name, email, phone)
            )
            self._conn.commit()
            return cur.lastrowid
        except sqlite3.IntegrityError:
            raise ValueError(f"Email already exists: {email}")

    def get(self, contact_id):
        row = self._conn.execute(
            "SELECT * FROM contacts WHERE id = ?", (contact_id,)
        ).fetchone()
        return dict(row) if row else None

    def list_all(self):
        return [dict(r) for r in self._conn.execute("SELECT * FROM contacts ORDER BY name")]

    def update(self, contact_id, **fields):
        if not fields:
            return
        cols = ", ".join(f"{k} = ?" for k in fields)
        self._conn.execute(
            f"UPDATE contacts SET {cols} WHERE id = ?",
            (*fields.values(), contact_id)
        )
        self._conn.commit()

    def delete(self, contact_id):
        self._conn.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
        self._conn.commit()

    def close(self):
        self._conn.close()


# ─── Run the CRUD lifecycle ───────────────────────────────────────────────────

db = ContactDB()

id1 = db.add("Alice", "alice@example.com", "555-1111")
id2 = db.add("Bob",   "bob@example.com",   "555-2222")
id3 = db.add("Carol", "carol@example.com")

print("All contacts:")
for c in db.list_all():
    print(" ", c)

print("\nGet Bob:", db.get(id2))

db.update(id1, phone="555-9999")
print("Alice after update:", db.get(id1))

db.delete(id3)
print("\nAfter deleting Carol:")
for c in db.list_all():
    print(" ", c)

# Duplicate email should raise:
try:
    db.add("Duplicate", "alice@example.com")
except ValueError as e:
    print("\nExpected error:", e)

db.close()
os.remove(DB)
