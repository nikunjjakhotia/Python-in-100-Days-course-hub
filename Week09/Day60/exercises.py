# Day 60 – UPDATE, DELETE & Transactions

import sqlite3, os

DB = "day60.db"

with sqlite3.connect(DB) as conn:
    conn.execute("""
        CREATE TABLE IF NOT EXISTS inventory (
            id       INTEGER PRIMARY KEY AUTOINCREMENT,
            product  TEXT NOT NULL UNIQUE,
            stock    INTEGER NOT NULL DEFAULT 0,
            price    REAL NOT NULL
        )
    """)
    conn.executemany(
        "INSERT INTO inventory (product, stock, price) VALUES (?, ?, ?)",
        [("Apple", 100, 0.50), ("Banana", 80, 0.30), ("Cherry", 50, 1.20), ("Date", 0, 2.50)]
    )
    conn.commit()


# Exercise 1: Update the price of "Apple" to 0.60 and confirm the change.
with sqlite3.connect(DB) as conn:
    conn.execute("UPDATE inventory SET price = ? WHERE product = ?", (0.60, "Apple"))
    conn.commit()
    row = conn.execute("SELECT price FROM inventory WHERE product = 'Apple'").fetchone()
    print("Apple new price:", row[0])


# Exercise 2: Deduct 10 from the stock of every product that has stock > 0.
with sqlite3.connect(DB) as conn:
    conn.execute("UPDATE inventory SET stock = stock - 10 WHERE stock > 0")
    conn.commit()
    for row in conn.execute("SELECT product, stock FROM inventory"):
        print(row)


# Exercise 3: Delete all products where stock = 0.
with sqlite3.connect(DB) as conn:
    conn.execute("DELETE FROM inventory WHERE stock = 0")
    conn.commit()
    remaining = conn.execute("SELECT COUNT(*) FROM inventory").fetchone()[0]
    print("Remaining products:", remaining)


# Exercise 4: Demonstrate a transaction rollback.
# Attempt two updates; the second one intentionally violates a constraint.
conn = sqlite3.connect(DB)
try:
    conn.execute("UPDATE inventory SET price = 1.00 WHERE product = 'Banana'")
    conn.execute("UPDATE inventory SET price = -5.00 WHERE product = 'Cherry'")
    # Manually raise to simulate a problem
    raise ValueError("Simulated error mid-transaction")
    conn.commit()
except Exception as e:
    conn.rollback()
    print("Rolled back due to:", e)
finally:
    conn.close()

os.remove(DB)
