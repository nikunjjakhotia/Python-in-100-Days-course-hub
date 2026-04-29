<!-- assignments-nav -->
[🏠 Home](../../) | [📚 Week 04 Lessons — Error Handling & File I/O](../../Week04/)

---
<!-- assignments-nav -->

# Week 04 Assignment: Build a Student Grade Manager

**Days 22–28 · Topics: try/except, Custom Exceptions, Text Files, CSV, JSON, Context Managers**

Using the error handling and file I/O skills from Days 22–28, build a CLI app that manages student grades with full validation, persistence, and reporting.

## What to Build
- Load and save student records (name, subject, score) from a CSV file using `csv` and `with open()`
- Add, update, and delete records with a custom `ValidationError` for invalid scores (below 0 or above 100)
- Calculate class average, highest score, and grade distribution (A/B/C/D/F) and display them in the CLI
- Export a JSON summary report at the end of each session
- Append every operation with a timestamp to `grades.log` using a context manager in append mode
