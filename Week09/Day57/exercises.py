# Day 57 – Intro to SQL & SQLite

import sqlite3, os

DB = "day57.db"

# Exercise 1: Connect to a SQLite database and print the SQLite version.

# Solution:
with sqlite3.connect(DB) as conn:
    version = conn.execute("SELECT sqlite_version()").fetchone()[0]
    print("SQLite version:", version)


# Exercise 2: Create a 'students' table with id, name, and grade columns.

# Solution:
with sqlite3.connect(DB) as conn:
    conn.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id    INTEGER PRIMARY KEY AUTOINCREMENT,
            name  TEXT NOT NULL,
            grade INTEGER NOT NULL
        )
    """)
    conn.commit()
print("students table created.")


# Exercise 3: Check whether the 'students' table exists using sqlite_master.

# Solution:
with sqlite3.connect(DB) as conn:
    result = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='students'"
    ).fetchone()
    print("Table exists:", result is not None)


# Exercise 4: Drop the 'students' table and confirm it no longer exists.

# Solution:
with sqlite3.connect(DB) as conn:
    conn.execute("DROP TABLE IF EXISTS students")
    conn.commit()
    result = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table' AND name='students'"
    ).fetchone()
    print("Table still exists:", result is not None)

# Clean up
os.remove(DB)
