# Day 58 – Creating Tables & Inserting Data

import sqlite3, os

DB = "day58.db"

def setup(conn):
    conn.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id      INTEGER PRIMARY KEY AUTOINCREMENT,
            title   TEXT NOT NULL,
            author  TEXT NOT NULL,
            year    INTEGER,
            price   REAL NOT NULL DEFAULT 0.0
        )
    """)
    conn.commit()


# Exercise 1: Insert a single book and print its auto-generated id.

# Solution:
with sqlite3.connect(DB) as conn:
    setup(conn)
    cur = conn.execute(
        "INSERT INTO books (title, author, year, price) VALUES (?, ?, ?, ?)",
        ("The Pragmatic Programmer", "Hunt & Thomas", 1999, 49.99)
    )
    conn.commit()
    print("Inserted book id:", cur.lastrowid)


# Exercise 2: Insert five books using executemany.

# Solution:
BOOKS = [
    ("Clean Code",               "Robert C. Martin", 2008, 35.00),
    ("Python Crash Course",      "Eric Matthes",     2019, 29.99),
    ("Fluent Python",            "Luciano Ramalho",  2022, 59.99),
    ("Design Patterns",          "Gang of Four",     1994, 44.99),
    ("You Don't Know JS",        "Kyle Simpson",     2015, 24.99),
]
with sqlite3.connect(DB) as conn:
    conn.executemany(
        "INSERT INTO books (title, author, year, price) VALUES (?, ?, ?, ?)",
        BOOKS
    )
    conn.commit()
print("5 books inserted.")


# Exercise 3: Try inserting a book with a NULL title; catch the error.

# Solution:
try:
    with sqlite3.connect(DB) as conn:
        conn.execute("INSERT INTO books (title, author, price) VALUES (?, ?, ?)", (None, "X", 5.0))
        conn.commit()
except sqlite3.IntegrityError as e:
    print("Caught expected error:", e)


# Clean up
os.remove(DB)
