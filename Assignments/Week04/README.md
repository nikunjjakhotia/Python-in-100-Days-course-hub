<!-- assignments-nav -->
[🏠 Home](../../) | [📚 Week 04 Lessons — Error Handling & File I/O](../../Week04/)

---
<!-- assignments-nav -->

# Week 04 Assignments — Error Handling & File I/O

**Days 22–28 · Topics: try/except, Custom Exceptions, Text Files, CSV, JSON, Context Managers**

---

## Assignments

### Day 22 — try / except / finally
- Write a `safe_divide(a, b)` function that catches ZeroDivisionError
- Write a file reader that catches FileNotFoundError and PermissionError
- Write a loop that retries user input up to 3 times before giving up

### Day 23 — Custom Exceptions
- Define a `ValidationError` exception with a message and field name
- Raise `InsufficientFundsError` in a bank account class
- Create an exception hierarchy: `AppError → DatabaseError, NetworkError`

### Day 24 — Reading & Writing Text Files
- Read a text file and count words, lines, and unique words
- Write a log function that appends timestamped messages to `app.log`
- Copy a file line-by-line, uppercasing every line

### Day 25 — CSV Files
- Read a CSV of products and calculate total value (quantity × price)
- Write a CSV report of students sorted by score descending
- Merge two CSV files on a shared "id" column

### Day 26 — JSON Files
- Read a JSON config file with defaults; override only keys that are present
- Write a `save_state(data, path)` and `load_state(path)` pair
- Convert a list of dicts to pretty-printed JSON and back

### Day 27 — Context Managers & with
- Write a custom context manager `Timer` that prints elapsed seconds
- Write a context manager `TempFile` that creates a temp file and deletes it on exit
- Explain (with code) why `with open(...)` is safer than `open()` / `close()`

### Day 28 — Project: Student Grade Manager
- Add import/export from CSV
- Add a "class average" and "grade distribution" report
- Persist data to JSON between runs

---

## Grading Criteria

| Criteria | Points |
|----------|--------|
| Correct error handling (right exceptions caught) | 40 |
| File operations work correctly | 30 |
| Edge cases (empty files, bad data) | 20 |
| Code style & docstrings | 10 |
| **Total** | **100** |
