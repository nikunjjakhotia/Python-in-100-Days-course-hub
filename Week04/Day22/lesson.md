<!-- nav -->
[← Day 21](../../Week03/Day21/lesson.md) | [🏠 Home](../../) | [Day 23 →](../Day23/lesson.md)

---
<!-- nav -->

# Day 22 – try / except / finally

## Learning Objectives
- Handle runtime errors gracefully with `try/except`
- Use multiple `except` blocks for different error types
- Use `finally` for cleanup code that always runs

---

## Core Concept

Without error handling, a crash stops your whole program. `try/except` lets you handle errors and keep running.

```python
try:
    x = int(input("Enter a number: "))
    print(10 / x)
except ValueError:
    print("That's not a valid number!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
```

---

## Common Built-in Exceptions

| Exception | Cause |
|---|---|
| `ValueError` | Wrong type of value (e.g. `int("abc")`) |
| `ZeroDivisionError` | Division by zero |
| `FileNotFoundError` | File doesn't exist |
| `IndexError` | List index out of range |
| `KeyError` | Dictionary key not found |
| `TypeError` | Wrong data type in operation |

---

## else Clause

Runs only if no exception was raised.

```python
try:
    result = 10 / 2
except ZeroDivisionError:
    print("Error!")
else:
    print(f"Success: {result}")
```

---

## finally Clause

Always runs — perfect for closing files or database connections.

```python
try:
    f = open("data.txt")
    data = f.read()
except FileNotFoundError:
    print("File not found.")
finally:
    print("Done attempting to read file.")
```

---

## Catching All Exceptions (use sparingly)

```python
try:
    risky_operation()
except Exception as e:
    print(f"Unexpected error: {e}")
```

---

## Key Takeaways
- Be specific — catch the exact exception you expect
- `finally` is for cleanup, not error messages
- Never silently swallow exceptions with a bare `except:`

---

## Exercises
See `exercises.py`

---

<!-- nav -->
[📝 Exercises](https://github.com/nikunjjakhotia/Python-in-100-Days-course-hub/blob/main/Week04/Day22/exercises.py) | [← Day 21](../../Week03/Day21/lesson.md) | [Day 23 →](../Day23/lesson.md)
<!-- nav -->
