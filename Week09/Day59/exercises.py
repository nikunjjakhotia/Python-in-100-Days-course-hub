# Day 59 – SELECT Queries & Filtering

import sqlite3, os

DB = "day59.db"

# Seed data
with sqlite3.connect(DB) as conn:
    conn.execute("""
        CREATE TABLE IF NOT EXISTS employees (
            id         INTEGER PRIMARY KEY AUTOINCREMENT,
            name       TEXT NOT NULL,
            department TEXT NOT NULL,
            salary     REAL NOT NULL
        )
    """)
    conn.executemany(
        "INSERT INTO employees (name, department, salary) VALUES (?, ?, ?)",
        [
            ("Alice",   "Engineering", 95000),
            ("Bob",     "Marketing",   70000),
            ("Carol",   "Engineering", 110000),
            ("Dave",    "HR",          65000),
            ("Eve",     "Engineering", 88000),
            ("Frank",   "Marketing",   75000),
        ]
    )
    conn.commit()


# Exercise 1: Select all employees and print them as dicts.
with sqlite3.connect(DB) as conn:
    conn.row_factory = sqlite3.Row
    for row in conn.execute("SELECT * FROM employees"):
        print(dict(row))


# Exercise 2: List Engineering employees, sorted by salary descending.
with sqlite3.connect(DB) as conn:
    conn.row_factory = sqlite3.Row
    rows = conn.execute(
        "SELECT name, salary FROM employees WHERE department = ? ORDER BY salary DESC",
        ("Engineering",)
    ).fetchall()
    print("\nEngineering salaries:")
    for r in rows:
        print(f"  {r['name']}: ${r['salary']:,.0f}")


# Exercise 3: Print the average salary and headcount per department.
with sqlite3.connect(DB) as conn:
    rows = conn.execute(
        "SELECT department, COUNT(*) AS n, AVG(salary) AS avg_sal FROM employees GROUP BY department"
    ).fetchall()
    print("\nDepartment summary:")
    for dept, n, avg in rows:
        print(f"  {dept:<15} {n} staff  avg ${avg:,.0f}")


# Exercise 4: Find the top-2 highest-paid employees overall.
with sqlite3.connect(DB) as conn:
    conn.row_factory = sqlite3.Row
    rows = conn.execute(
        "SELECT name, salary FROM employees ORDER BY salary DESC LIMIT 2"
    ).fetchall()
    print("\nTop 2 earners:")
    for r in rows:
        print(f"  {r['name']}: ${r['salary']:,.0f}")

os.remove(DB)
