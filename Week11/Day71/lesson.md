<!-- nav -->
[← Day 70](../../Week10/Day70/lesson.md) | [🏠 Home](../../) | [Day 72 →](../Day72/lesson.md)

---
<!-- nav -->

# Day 71 – File System Automation with `pathlib` & `shutil`

## Learning Objectives
- Navigate the file system with `pathlib.Path`
- Copy, move, rename, and delete files with `shutil`
- Glob for files matching a pattern

---

## `pathlib.Path` Basics

```python
from pathlib import Path

p = Path(".")                   # current directory
home = Path.home()              # C:\Users\you  or  /home/you
docs = home / "Documents"       # path joining with /

print(p.resolve())              # absolute path
print(p.exists())
print(p.is_dir())
print(p.is_file())
```

---

## Listing & Globbing

```python
# All items in a directory
for item in Path(".").iterdir():
    print(item.name, item.stat().st_size)

# Recursive glob — all Python files
for f in Path(".").rglob("*.py"):
    print(f)

# Non-recursive glob — only this level
for f in Path(".").glob("*.txt"):
    print(f)
```

---

## Creating & Deleting

```python
Path("new_dir").mkdir(parents=True, exist_ok=True)
Path("notes.txt").write_text("Hello!\n")
Path("notes.txt").unlink()        # delete file
Path("new_dir").rmdir()           # delete empty directory
```

---

## `shutil` — Copy, Move, Delete Tree

```python
import shutil

shutil.copy("src.txt", "dst.txt")            # copy file
shutil.copytree("src_dir", "dst_dir")        # copy whole tree
shutil.move("old_name.txt", "new_name.txt")  # rename / move
shutil.rmtree("old_dir")                     # delete directory tree
```

---

## File Metadata

```python
stat = Path("notes.txt").stat()
print(stat.st_size)      # bytes
print(stat.st_mtime)     # modified timestamp (float)

from datetime import datetime
print(datetime.fromtimestamp(stat.st_mtime))
```

---

## Key Takeaways
- `pathlib.Path` replaces `os.path` with an object-oriented API — prefer it
- `/` operator joins path parts cleanly
- `shutil` handles multi-file operations that `Path` doesn't cover

---

## Exercises
See `exercises.py`

---

<!-- nav -->
[📝 Exercises](https://github.com/nikunjjakhotia/Python-in-100-Days-course-hub/blob/main/Week11/Day71/exercises.py) | [🏠 Home](/Python-in-100-Days-course-hub/) | [← Day 70](../../Week10/Day70/lesson.md) | [Day 72 →](../Day72/lesson.md)
<!-- nav -->
