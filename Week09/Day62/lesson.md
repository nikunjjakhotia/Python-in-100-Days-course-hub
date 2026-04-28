<!-- nav -->
[← Day 61](../Day61/lesson.md) | [🏠 Home](../../) | [Day 63 →](../Day63/lesson.md)

---
<!-- nav -->

# Day 62 – Building a CRUD App

## Learning Objectives
- Wrap database operations in a clean class
- Implement Create, Read, Update, Delete through Python functions
- Handle duplicate-key and not-found errors gracefully

---

## CRUD Pattern

| Operation | SQL | Python method |
|-----------|-----|---------------|
| Create | INSERT | `add()` |
| Read | SELECT | `get()`, `list_all()` |
| Update | UPDATE | `update()` |
| Delete | DELETE | `delete()` |

---

## Database Class Template

```python
import sqlite3

class ContactDB:
    def __init__(self, path="contacts.db"):
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
        return [dict(r) for r in self._conn.execute("SELECT * FROM contacts")]

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
```

---

## Key Takeaways
- Encapsulate database logic in a class — callers never write raw SQL
- Catch `IntegrityError` for constraint violations (duplicates, not-null)
- Commit after every write; roll back on error

---

## Exercises
See `exercises.py`

---

<!-- nav -->
[📝 Exercises](exercises.py) | [← Day 61](../Day61/lesson.md) | [Day 63 →](../Day63/lesson.md)
<!-- nav -->
