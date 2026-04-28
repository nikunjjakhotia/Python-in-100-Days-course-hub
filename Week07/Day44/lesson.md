<!-- nav -->
[← Day 43](../Day43/lesson.md) | [🏠 Home](../../) | [Day 45 →](../Day45/lesson.md)

---
<!-- nav -->

# Day 44 – Standard Library Highlights

## Learning Objectives
- Use `os`, `sys`, `math`, `random`, and `datetime` from the standard library
- Know which module to reach for common tasks

---

## `os` — Operating System Interface

```python
import os

print(os.getcwd())              # current working directory
print(os.listdir("."))          # list files/folders
os.makedirs("new_dir", exist_ok=True)
print(os.path.exists("new_dir"))  # True
print(os.path.join("folder", "file.txt"))  # folder/file.txt
```

---

## `sys` — Interpreter Info

```python
import sys

print(sys.version)      # Python version string
print(sys.platform)     # 'win32', 'linux', 'darwin'
print(sys.argv)         # command-line arguments list
sys.exit(0)             # exit the program (0 = success)
```

---

## `math` — Mathematical Functions

```python
import math

print(math.sqrt(25))        # 5.0
print(math.ceil(4.2))       # 5
print(math.floor(4.9))      # 4
print(math.log(100, 10))    # 2.0
print(math.pi, math.e)      # 3.14159..., 2.71828...
```

---

## `random` — Randomness

```python
import random

print(random.randint(1, 10))          # integer 1–10 inclusive
print(random.choice(["a","b","c"]))   # random element
items = [1, 2, 3, 4, 5]
random.shuffle(items)
print(items)                           # shuffled list
print(random.random())                 # float 0.0–1.0
```

---

## `datetime` — Dates and Times

```python
from datetime import datetime, date, timedelta

now   = datetime.now()
today = date.today()
print(now.strftime("%Y-%m-%d %H:%M:%S"))
print(today + timedelta(days=7))   # one week from today
```

---

## Key Takeaways
- The standard library covers almost every common task — check it before installing a package
- `os` / `sys` for system interaction, `math` for numbers, `random` for randomness, `datetime` for time

---

## Exercises
See `exercises.py`

---

<!-- nav -->
[📝 Exercises](exercises.py) | [← Day 43](../Day43/lesson.md) | [Day 45 →](../Day45/lesson.md)
<!-- nav -->
