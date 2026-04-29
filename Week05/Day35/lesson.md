<!-- nav -->
[← Day 34](../Day34/lesson.md) | [🏠 Home](../../) | [Day 36 →](../../Week06/Day36/lesson.md)

---
<!-- nav -->

# Day 35 – Project: Student Report Generator

## What You're Building
A Python script that takes a list of student records, calculates per-subject and overall averages, assigns letter grades, and writes a formatted report to a text file.

---

## Learning Objectives
- Combine nested dicts, list comprehensions, sorting, and file I/O
- Apply a grading formula across multiple records
- Write a clean, formatted report

---

## Project Spec

### Input Data (hardcoded or from a CSV):
```python
students = [
    {"name": "Alice",   "Math": 92, "Science": 88, "English": 95},
    {"name": "Bob",     "Math": 74, "Science": 65, "English": 80},
    {"name": "Charlie", "Math": 55, "Science": 70, "English": 62},
]
```

### Output: `student_report.txt`
```
========== STUDENT REPORT ==========
Name       Math  Science  English  Avg   Grade
-------------------------------------------
Alice        92       88       95  91.7  A
Bob          74       65       80  73.0  C
Charlie      55       70       62  62.3  D
-------------------------------------------
Class avg:   73.7
=====================================
```

---

## Grading Scale:
| Range | Grade |
|---|---|
| 90+ | A |
| 80+ | B |
| 70+ | C |
| 60+ | D |
| <60 | F |

---

## Skills Used
- List of dicts, list comprehensions
- `sorted()` with lambda
- String formatting with f-strings and `.format()`
- File writing

---

## Starter Code
See `exercises.py` for the full project.

---

## 📝 Week 5 Assignment

You've completed Week 5! Time to put it all together.

**[→ Complete the Week 5 Assignment](../../Assignments/Week05/)**

---

<!-- nav -->
[📝 Exercises](https://github.com/nikunjjakhotia/Python-in-100-Days-course-hub/blob/main/Week05/Day35/exercises.py) | [🏠 Home](/Python-in-100-Days-course-hub/) | [← Day 34](../Day34/lesson.md) | [Day 36 →](../../Week06/Day36/lesson.md)
<!-- nav -->
