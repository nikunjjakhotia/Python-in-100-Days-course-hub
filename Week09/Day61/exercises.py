# Day 61 – Python sqlite3 Module Deep Dive

import sqlite3, os

DB = "day61.db"

# Setup: two related tables
with sqlite3.connect(DB) as conn:
    conn.executescript("""
        CREATE TABLE IF NOT EXISTS authors (
            id   INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        );
        CREATE TABLE IF NOT EXISTS books (
            id        INTEGER PRIMARY KEY AUTOINCREMENT,
            title     TEXT NOT NULL,
            author_id INTEGER NOT NULL REFERENCES authors(id),
            year      INTEGER
        );
        INSERT OR IGNORE INTO authors (name) VALUES ('George Orwell'), ('J.K. Rowling'), ('Tolkien');
        INSERT OR IGNORE INTO books (title, author_id, year) VALUES
            ('1984',                     1, 1949),
            ('Animal Farm',              1, 1945),
            ('Harry Potter 1',           2, 1997),
            ('Harry Potter 2',           2, 1998),
            ('The Fellowship of the Ring', 3, 1954);
    """)


# Exercise 1: Use sqlite3.Row to fetch all books and print as dicts.
with sqlite3.connect(DB) as conn:
    conn.row_factory = sqlite3.Row
    for row in conn.execute("SELECT * FROM books"):
        print(dict(row))


# Exercise 2: JOIN books and authors to print "Title – Author (Year)".
with sqlite3.connect(DB) as conn:
    conn.row_factory = sqlite3.Row
    rows = conn.execute("""
        SELECT books.title, authors.name AS author, books.year
        FROM books JOIN authors ON books.author_id = authors.id
        ORDER BY books.year
    """).fetchall()
    print()
    for r in rows:
        print(f"{r['title']} – {r['author']} ({r['year']})")


# Exercise 3: Count books per author using GROUP BY.
with sqlite3.connect(DB) as conn:
    rows = conn.execute("""
        SELECT authors.name, COUNT(books.id) AS total
        FROM authors LEFT JOIN books ON books.author_id = authors.id
        GROUP BY authors.id
    """).fetchall()
    print()
    for name, total in rows:
        print(f"{name}: {total} book(s)")


# Exercise 4: List all table names in the database using sqlite_master.
with sqlite3.connect(DB) as conn:
    tables = conn.execute(
        "SELECT name FROM sqlite_master WHERE type='table'"
    ).fetchall()
    print("\nTables:", [t[0] for t in tables])

os.remove(DB)
