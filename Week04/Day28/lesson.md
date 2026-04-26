# Day 28 – Project: Log Analyzer

## What You're Building
A command-line tool that reads a server log file, parses each entry, and produces a summary report showing error counts, warning counts, and the top error messages.

---

## Learning Objectives
- Combine file I/O, error handling, string parsing, and dictionaries
- Write a reusable analysis function
- Generate a formatted text report

---

## Project Spec

### Input: `server.log`
```
2025-01-10 08:23:01 INFO  Server started on port 8080
2025-01-10 08:24:15 ERROR Database connection refused
2025-01-10 08:24:20 WARNING Retrying connection (1/3)
2025-01-10 08:30:00 ERROR Database connection refused
2025-01-10 08:31:05 INFO  User 'admin' logged in
2025-01-10 09:00:00 ERROR Disk quota exceeded
```

### Output: `report.txt`
```
===== LOG ANALYSIS REPORT =====
Total entries  : 6
INFO           : 2
WARNING        : 1
ERROR          : 3

Top Errors:
  1x - Disk quota exceeded
  2x - Database connection refused
================================
```

---

## Skills Used
- File reading (line by line)
- String splitting and parsing
- Dictionary counting
- `sorted()` with lambda
- File writing

---

## Starter Code
See `exercises.py` for the full project.

---

## Bonus Challenges
1. Accept the log filename as a command-line argument (`sys.argv`)
2. Filter entries by date range
3. Export the report in JSON format
