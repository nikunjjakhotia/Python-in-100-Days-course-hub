<!-- nav -->
[← Day 25](../Day25/lesson.md) | [🏠 Home](../../) | [Day 27 →](../Day27/lesson.md)

---
<!-- nav -->

# Day 26 – os & pathlib

## Learning Objectives
- Navigate and manipulate the filesystem with `os` and `pathlib`
- List, create, rename, and delete files and directories
- Build cross-platform paths

---

## os Module Essentials

```python
import os

os.getcwd()               # current working directory
os.listdir(".")           # list files in a directory
os.makedirs("a/b/c")      # create nested directories
os.rename("old.txt", "new.txt")
os.remove("file.txt")     # delete a file
os.rmdir("empty_dir")     # delete an empty directory
os.path.exists("file.txt")  # check if path exists
os.path.join("folder", "file.txt")  # safe path building
```

---

## pathlib — Modern Alternative (Python 3.4+)

`pathlib.Path` objects are cleaner than string-based `os.path`.

```python
from pathlib import Path

p = Path("data/logs")
p.mkdir(parents=True, exist_ok=True)

log_file = p / "app.log"    # / operator builds paths
log_file.write_text("Started\n")
print(log_file.read_text())
print(log_file.exists())
log_file.unlink()           # delete the file
```

---

## Listing Files by Extension

```python
from pathlib import Path

py_files = list(Path(".").glob("**/*.py"))
for f in py_files:
    print(f)
```

---

## File Metadata

```python
import os
stat = os.stat("file.txt")
print(stat.st_size)   # size in bytes
```

---

## Key Takeaways
- Prefer `pathlib` for new code — it's more readable and object-oriented
- Use `os.path.join()` or `Path /` to build paths — never hardcode separators
- `exist_ok=True` prevents errors when a directory already exists

---

## Exercises
See `exercises.py`

---

<!-- nav -->
[📝 Exercises](https://github.com/nikunjjakhotia/Python-in-100-Days-course-hub/blob/main/Week04/Day26/exercises.py) | [🏠 Home](/Python-in-100-Days-course-hub/) | [← Day 25](../Day25/lesson.md) | [Day 27 →](../Day27/lesson.md)
<!-- nav -->
