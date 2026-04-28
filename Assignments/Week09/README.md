<!-- assignments-nav -->
[🏠 Home](../../) | [📚 Week 09 Lessons — SQLite & Databases](../../Week09/)

---
<!-- assignments-nav -->

# Week 09 Assignments — SQLite & Databases

**Days 57–63 · Topics: SQL Basics, INSERT/SELECT/UPDATE/DELETE, Transactions, CRUD, sqlite3**

---

## Assignments

### Day 57 — Intro to SQLite
- Create a `library.db` with a `books` table and verify it via `sqlite_master`
- Print the SQLite version and list all tables
- Drop and recreate the table; confirm it's empty

### Day 58 — Inserting Data
- Insert 10 books using `executemany`
- Confirm `lastrowid` returns the correct id for a single insert
- Attempt to insert a NULL title and handle the IntegrityError

### Day 59 — SELECT Queries
- Query books published after 2010, sorted by year
- Print the average price and total count of all books
- Fetch exactly the top-3 most expensive books

### Day 60 — UPDATE & DELETE
- Give all books in the "tech" category a 10% price increase
- Delete books with price < $5.00
- Demonstrate a rollback when a mid-transaction error occurs

### Day 61 — sqlite3 Deep Dive
- Use `sqlite3.Row` to access columns by name
- Write a JOIN query across `books` and `authors` tables
- Use `executescript` to run a schema migration

### Day 62 — CRUD App
- Implement full CRUD for a `movies` database
- Add a `search(keyword)` method that matches partial titles
- Handle the IntegrityError for duplicate titles

### Day 63 — Project: To-Do App
- Add due-date support; highlight overdue tasks
- Add a `list done` and `list pending` filter option
- Export all tasks to `tasks.csv`

---

## Grading Criteria

| Criteria | Points |
|----------|--------|
| Correct SQL (parameterised) | 40 |
| CRUD operations work | 30 |
| Error handling (IntegrityError, rollback) | 20 |
| Code organisation | 10 |
| **Total** | **100** |
