<!-- nav -->
[← Day 26](../Day26/lesson.md) | [🏠 Home](../../) | [Day 28 →](../Day28/lesson.md)

---
<!-- nav -->

# Day 27 – File I/O Challenges

## Learning Objectives
- Apply reading and writing skills to realistic data scenarios
- Combine loops, conditions, and file I/O
- Handle common I/O edge cases

---

## Challenge 1: Word Counter

Read a file and count total words, lines, and unique words.

```python
with open("text.txt") as f:
    content = f.read()

words = content.lower().split()
print(f"Lines: {content.count(chr(10)) + 1}")
print(f"Words: {len(words)}")
print(f"Unique: {len(set(words))}")
```

---

## Challenge 2: Search & Replace in a File

```python
with open("input.txt") as f:
    content = f.read()

modified = content.replace("Python", "Python 3")

with open("output.txt", "w") as f:
    f.write(modified)
```

---

## Challenge 3: Merge Multiple Files

```python
import glob

with open("merged.txt", "w") as out:
    for filename in sorted(glob.glob("part_*.txt")):
        with open(filename) as f:
            out.write(f.read())
            out.write("\n")
```

---

## Challenge 4: Filter Lines by Keyword

```python
with open("log.txt") as f:
    errors = [line for line in f if "ERROR" in line]

with open("errors_only.txt", "w") as f:
    f.writelines(errors)
```

---

## Key Takeaways
- String methods like `.replace()`, `.split()`, `.strip()` are essential for text processing
- Always strip whitespace when comparing or counting
- List comprehensions work naturally when reading file lines

---

## Exercises
See `exercises.py`

---

<!-- nav -->
[📝 Exercises](https://github.com/nikunjjakhotia/Python-in-100-Days-course-hub/blob/main/Week04/Day27/exercises.py) | [← Day 26](../Day26/lesson.md) | [Day 28 →](../Day28/lesson.md)
<!-- nav -->
