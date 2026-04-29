<!-- assignments-nav -->
[🏠 Home](../../) | [📚 Week 07 Lessons — Modules & Packages](../../Week07/)

---
<!-- assignments-nav -->

# Week 07 Assignment: Build a Personal Utility Package

**Days 43–49 · Topics: Modules, Standard Library, Custom Packages, venv, pip**

Using the module and packaging skills from Days 43–49, create a reusable Python package called `pyutils` with three well-organised modules and install it locally in a virtual environment.

## What to Build
- A `pyutils/` package with an `__init__.py` that re-exports key functions from three modules:
  - `strings.py`: `word_count(text)`, `truncate(text, n)`, `slug(text)`
  - `dates.py`: `days_until(date)`, `format_date(date, fmt)`, `is_weekend(date)`
  - `validators.py`: `is_email(s)`, `is_phone(s)`, `is_url(s)`
- A `requirements.txt` and a virtual environment (not committed) to isolate any dependencies
- A `demo.py` script that exercises every function with printed output
- A `README.md` inside the package folder that describes each module and its functions
