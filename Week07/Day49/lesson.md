<!-- nav -->
[← Day 48](../Day48/lesson.md) | [🏠 Home](../../) | [Day 50 →](../../Week08/Day50/lesson.md)

---
<!-- nav -->

# Day 49 – Project: Build a Reusable Utility Library

## What You're Building
A small personal utility package called `pyutils` with three modules:
- `pyutils/strings.py` — string helpers
- `pyutils/numbers.py` — numeric helpers
- `pyutils/dates.py`   — date helpers

---

## Learning Objectives
- Organise code into a proper package with `__init__.py`
- Write clean, well-named functions with type hints
- Use `if __name__ == "__main__"` demo blocks

---

## Project Spec

### `pyutils/strings.py`
```python
def slugify(text: str) -> str:
    """Convert 'Hello World!' → 'hello-world'"""

def truncate(text: str, max_len: int, suffix: str = "...") -> str:
    """Truncate to max_len characters, appending suffix if cut."""

def word_count(text: str) -> dict:
    """Return {word: frequency} dict (case-insensitive)."""
```

### `pyutils/numbers.py`
```python
def clamp(value: float, lo: float, hi: float) -> float:
    """Return value constrained to [lo, hi]."""

def percentage(part: float, total: float) -> float:
    """Return part/total * 100 rounded to 2 dp."""

def is_prime(n: int) -> bool:
    """Return True if n is a prime number."""
```

### `pyutils/dates.py`
```python
from datetime import date, timedelta

def days_until(target: date) -> int:
    """Days from today to target (negative if past)."""

def date_range(start: date, end: date):
    """Yield every date from start up to (but not including) end."""

def friendly(d: date) -> str:
    """Return 'Monday, 26 April 2026' style string."""
```

### `pyutils/__init__.py`
Re-export key functions so users can write `from pyutils import slugify`.

---

## Stretch Goals
- Add docstrings and type hints to every function
- Write a `demo.py` at the root that shows all functions in action
- Add a `__version__ = "1.0.0"` to `__init__.py`

---

## Exercises
See `exercises.py`

---

## 📝 Week 7 Assignment

You've completed Week 7! Time to put it all together.

**[→ Complete the Week 7 Assignment](../../Assignments/Week07/)**

---

<!-- nav -->
[📝 Exercises](https://github.com/nikunjjakhotia/Python-in-100-Days-course-hub/blob/main/Week07/Day49/exercises.py) | [🏠 Home](/Python-in-100-Days-course-hub/) | [← Day 48](../Day48/lesson.md) | [Day 50 →](../../Week08/Day50/lesson.md)
<!-- nav -->
