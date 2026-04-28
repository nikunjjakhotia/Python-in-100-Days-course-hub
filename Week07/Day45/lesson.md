<!-- nav -->
[← Day 44](../Day44/lesson.md) | [🏠 Home](../../) | [Day 46 →](../Day46/lesson.md)

---
<!-- nav -->

# Day 45 – Creating Your Own Modules

## Learning Objectives
- Write a reusable module from scratch
- Import from a file in the same directory
- Avoid circular imports

---

## Writing a Module

A module is simply a `.py` file with functions, classes, or constants you want to reuse.

```
project/
├── main.py
└── greetings.py
```

```python
# greetings.py
def hello(name):
    return f"Hello, {name}!"

def goodbye(name):
    return f"See you later, {name}!"

GREETING_COUNT = 0
```

```python
# main.py
from greetings import hello, goodbye

print(hello("Alice"))    # Hello, Alice!
print(goodbye("Bob"))    # See you later, Bob!
```

---

## Importing Everything (and why to avoid it)

```python
from greetings import *   # imports all public names
```

This can cause name collisions — prefer explicit imports.

---

## Reloading a Module (interactive sessions)

```python
import importlib
import greetings

importlib.reload(greetings)   # picks up changes without restarting Python
```

---

## Circular Imports

If `a.py` imports `b.py` and `b.py` imports `a.py`, Python raises an error.  
Fix: move the shared code into a third module `c.py`.

---

## Key Takeaways
- Any `.py` file is a module — just `import` it by filename (without `.py`)
- Keep modules focused on one topic
- Use `if __name__ == "__main__"` to prevent test code from running on import

---

## Exercises
See `exercises.py`

---

<!-- nav -->
[📝 Exercises](exercises.py) | [← Day 44](../Day44/lesson.md) | [Day 46 →](../Day46/lesson.md)
<!-- nav -->
