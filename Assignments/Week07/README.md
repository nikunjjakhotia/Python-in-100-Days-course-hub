<!-- assignments-nav -->
[🏠 Home](../../) | [📚 Week 07 Lessons — Modules & Packages](../../Week07/)

---
<!-- assignments-nav -->

# Week 7 Assignment — Reusable Utility Library

**Days 43–49 · Topics: Modules, Standard Library, Custom Packages, venv, pip**

Build a properly structured Python package called `pyutils` with three focused modules, install it in a virtual environment, and write a demo script that exercises every function.

---

## 🎯 What You'll Build

A reusable utility package that a developer could drop into any project — with clean imports, a virtual environment, and a `requirements.txt`.

---

## 📋 Requirements

1. Create a `pyutils/` directory with an `__init__.py` that re-exports all public functions so users can write `from pyutils import word_count`.
2. **`strings.py`** module: `word_count(text)` → int, `truncate(text, n, suffix="...")` → str, `slug(text)` → lowercase hyphenated URL slug.
3. **`dates.py`** module: `days_until(target_date)` → int, `format_date(date, fmt="%d %b %Y")` → str, `is_weekend(date)` → bool.
4. **`validators.py`** module: `is_email(s)` → bool (use `re`), `is_phone(s)` → bool (10–15 digits, optional leading `+`), `is_url(s)` → bool (must start with `http://` or `https://`).
5. Set up a **virtual environment** (`venv/`) and install at least one third-party library (e.g. `python-dateutil` for date parsing); record it in `requirements.txt`.
6. Write a `demo.py` at the repo root that imports from `pyutils` and prints the result of calling every function with at least one example argument.
7. All functions must include a one-line docstring describing what they return.
8. Add a `pyutils/README.md` (inside the package) listing each module, its functions, parameters, and return types in a markdown table.

---

## 💡 Hints

- `re.match(r"[^@]+@[^@]+\.[^@]+", s)` is a simple email pattern.
- `text.lower().replace(" ", "-")` is the core of `slug()` — also strip punctuation with `re.sub(r"[^\w\s-]", "", text)`.
- `(datetime.date.today() - target_date).days` gives signed day difference.
- Activate venv on Windows: `venv\Scripts\activate`; on Mac/Linux: `source venv/bin/activate`.

---

## 📤 How to Submit

1. Commit `pyutils/`, `demo.py`, and `requirements.txt` to this folder (do **not** commit `venv/`).
2. Run `demo.py` inside the activated virtual environment with no errors.
3. Share a screenshot of the `demo.py` output on LinkedIn with **#Python100Days** and tag [@nikunjjakhotia](https://www.linkedin.com/in/nikunjjakhotia/).

---

## ✅ Marking Criteria

| Criterion | Marks |
|-----------|-------|
| Package structure with correct `__init__.py` re-exports | /10 |
| All 3 modules implement their functions correctly | /15 |
| Virtual environment and `requirements.txt` set up properly | /10 |
| `demo.py` exercises every function with printed output | /10 |
| Docstrings present on all functions | /5 |
| **Total** | **/50** |

---

*If this course is helping you, please ⭐ [star the repo](https://github.com/nikunjjakhotia/Python-in-100-Days-course-hub) — it helps others find it!*
