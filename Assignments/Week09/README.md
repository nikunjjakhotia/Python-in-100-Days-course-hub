<!-- assignments-nav -->
[🏠 Home](../../) | [📚 Week 09 Lessons — SQLite & Databases](../../Week09/)

---
<!-- assignments-nav -->

# Week 09 Assignment: Build a Contact Database App

**Days 57–63 · Topics: SQL Basics, INSERT/SELECT/UPDATE/DELETE, Transactions, CRUD, sqlite3**

Using the SQLite and `sqlite3` skills from Days 57–63, build a full CRUD CLI app that stores, searches, and exports contacts.

## What to Build
- A `contacts.db` SQLite database with a `contacts` table: id, name, phone, email, city
- Full CRUD operations — add, view all, search by name or city, update, and delete — using parameterised queries throughout
- A transaction that bulk-inserts 5 sample contacts on first run and rolls back cleanly on any integrity error
- Export all contacts to `contacts.csv` using Python's `csv` module
- Use a `sqlite3.Row` factory so all columns are accessible by name throughout the app
