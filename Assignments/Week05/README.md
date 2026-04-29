<!-- assignments-nav -->
[🏠 Home](../../) | [📚 Week 05 Lessons — Advanced Data Structures](../../Week05/)

---
<!-- assignments-nav -->

# Week 5 Assignment — Library Catalogue

**Days 29–35 · Topics: List Comprehensions, Advanced Dicts, Sets, Nested Structures, Sorting & Filtering**

Build a CLI library catalogue that lets users browse, search, filter, and sort a collection of books using Python's built-in data structures.

---

## 🎯 What You'll Build

A book catalogue stored entirely in memory using lists, dicts, and sets — no database, no files — demonstrating fluency with Python's core data structures.

---

## 📋 Requirements

1. Store at least **15 books** as a list of dictionaries, each with: `title`, `author`, `genre`, `year`, `rating` (float 1.0–5.0), and `available` (bool).
2. Use a **set** to store unique genres and display the genre menu dynamically — no hardcoded genre lists.
3. Implement **search by title or author** using a list comprehension with a case-insensitive substring match.
4. Implement **filter by genre and availability** using a list comprehension with multiple conditions.
5. Implement **sort by rating (desc), year (desc), or title (asc)** using `sorted()` with a `key=` lambda.
6. Track a **"recently viewed"** list using `collections.deque(maxlen=5)` — update it on every book lookup.
7. Build a **summary dict** using `dict comprehension` that maps each genre to its average rating, rounded to 2 decimal places.
8. Display all results in a clean table format using f-string column alignment (e.g. `f"{title:<30} {author:<20} {rating:>4}`).

---

## 💡 Hints

- `{book['genre'] for book in catalogue}` builds a set of unique genres in one line.
- `key=lambda b: b['rating']` with `reverse=True` sorts by rating descending.
- `collections.deque(maxlen=5)` automatically drops the oldest entry when full.
- f-string alignment: `f"{'Title':<30}"` left-pads a field to 30 characters.

---

## 📤 How to Submit

1. Save your solution as `Week05_assignment.py` inside this folder.
2. Demo search, filter, sort, and the genre summary from the menu with no errors.
3. Share a screenshot of the sorted catalogue output on LinkedIn with **#Python100Days** and tag [@nikunjjakhotia](https://www.linkedin.com/in/nikunjjakhotia/).

---

## ✅ Marking Criteria

| Criterion | Marks |
|-----------|-------|
| 15+ books stored as list of dicts with all required fields | /10 |
| Search by title/author works case-insensitively | /10 |
| Filter by genre and availability works correctly | /10 |
| Sort by rating, year, and title all work | /10 |
| Genre average rating summary built with dict comprehension | /5 |
| Recently viewed deque updates and displays correctly | /5 |
| **Total** | **/50** |

---

*If this course is helping you, please ⭐ [star the repo](https://github.com/nikunjjakhotia/Python-in-100-Days-course-hub) — it helps others find it!*
