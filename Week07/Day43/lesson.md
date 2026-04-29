<!-- nav -->
[← Day 42](../../Week06/Day42/lesson.md) | [🏠 Home](../../) | [Day 44 →](../Day44/lesson.md)

---
<!-- nav -->

# Day 43 – Intro to Modules

## Learning Objectives
- Understand what a module is and why they exist
- Use `import`, `from ... import`, and `import ... as`
- Know the role of `__name__ == "__main__"`

---

## What Is a Module?

A **module** is any `.py` file. Importing it gives you access to the functions, classes, and variables defined inside it.

```python
import math
print(math.sqrt(16))   # 4.0
print(math.pi)         # 3.14159...
```

---

## Import Styles

```python
# Import the whole module
import math
print(math.floor(3.7))   # 3

# Import specific names
from math import sqrt, pi
print(sqrt(9))           # 3.0

# Alias to shorten a long name
import datetime as dt
print(dt.date.today())
```

---

## The `__name__` Guard

When Python runs a file directly, `__name__` equals `"__main__"`.  
When the file is *imported*, `__name__` equals the file name (without `.py`).

```python
# utils.py
def greet(name):
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("World"))  # only runs when executed directly
```

This lets a file be both a runnable script and a reusable module.

---

## Key Takeaways
- `import module` — access with `module.name`
- `from module import name` — access directly
- `import module as alias` — shorter name
- `if __name__ == "__main__"` — test/run code only when executed directly

---

## Exercises
See `exercises.py`

---

<!-- nav -->
[📝 Exercises](https://github.com/nikunjjakhotia/Python-in-100-Days-course-hub/blob/main/Week07/Day43/exercises.py) | [🏠 Home](/Python-in-100-Days-course-hub/) | [← Day 42](../../Week06/Day42/lesson.md) | [Day 44 →](../Day44/lesson.md)
<!-- nav -->
