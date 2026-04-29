<!-- assignments-nav -->
[🏠 Home](../../) | [📚 Week 04 Lessons — Error Handling & File I/O](../../Week04/)

---
<!-- assignments-nav -->

# Week 4 Assignment — Student Grade Manager

**Days 22–28 · Topics: try/except, Custom Exceptions, Text Files, CSV, JSON, Context Managers**

Build a CLI app that manages student grades with full input validation, persistent CSV storage, JSON reporting, and an activity log.

---

## 🎯 What You'll Build

A fully persistent grade tracker where records survive between runs, every operation is logged, and a JSON summary is generated on exit.

---

## 📋 Requirements

1. Store student records (name, subject, score 0–100) in a **CSV file** (`grades.csv`) — load on startup and save after every change using `with open()` and the `csv` module.
2. Support four operations from a menu: **Add**, **View all**, **Update score**, **Delete student**.
3. Define a custom `ValidationError(Exception)` raised whenever a score is below 0 or above 100; catch it and print a user-friendly message without crashing.
4. Calculate and display **class average**, **highest score**, and **grade distribution** (A: 90–100, B: 80–89, C: 70–79, D: 60–69, F: < 60) after every view.
5. On exit, export a **JSON summary** (`summary.json`) with: timestamp, total students, average score, and the grade distribution counts.
6. Append every operation (add/update/delete) with a **timestamp** to `grades.log` using a context manager in append mode.
7. Wrap all file operations in `try/except` — handle `FileNotFoundError` (first run) and `PermissionError` gracefully.
8. Prevent duplicate student names within the same subject — raise a `ValidationError` if the combination already exists.

---

## 💡 Hints

- `csv.DictReader` / `csv.DictWriter` let you work with rows as dictionaries.
- `datetime.datetime.now().isoformat()` gives a clean ISO timestamp.
- `json.dump(data, f, indent=2)` writes readable JSON.
- Build the grade distribution with a `collections.Counter` or a plain dict and `if/elif` chain.

---

## 📤 How to Submit

1. Save your solution as `Week04_assignment.py` inside this folder.
2. Run the app, add 5 students, update one, delete one, then exit to generate `summary.json`.
3. Share a screenshot of the grade distribution output on LinkedIn with **#Python100Days** and tag [@nikunjjakhotia](https://www.linkedin.com/in/nikunjjakhotia/).

---

## ✅ Marking Criteria

| Criterion | Marks |
|-----------|-------|
| CSV load/save works across restarts | /10 |
| All 4 CRUD operations function correctly | /10 |
| Custom `ValidationError` raised and caught properly | /10 |
| Class average, highest score, and distribution displayed | /10 |
| JSON summary exported on exit | /5 |
| Activity log appended with timestamps | /5 |
| **Total** | **/50** |

---

*If this course is helping you, please ⭐ [star the repo](https://github.com/nikunjjakhotia/Python-in-100-Days-course-hub) — it helps others find it!*
