<!-- nav -->
[← Day 24](../Day24/lesson.md) | [🏠 Home](../../) | [Day 26 →](../Day26/lesson.md)

---
<!-- nav -->

# Day 25 – Writing Files

## Learning Objectives
- Write and append to text files
- Create files programmatically
- Understand the difference between `"w"` and `"a"` modes

---

## Writing to a File

Mode `"w"` creates the file (or overwrites if it exists).

```python
with open("output.txt", "w") as f:
    f.write("Hello, file!\n")
    f.write("Second line.\n")
```

---

## Appending to a File

Mode `"a"` adds to the end without overwriting.

```python
with open("log.txt", "a") as f:
    f.write("New log entry\n")
```

---

## Writing Multiple Lines with writelines()

```python
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("output.txt", "w") as f:
    f.writelines(lines)
```

---

## Writing CSV Data Manually

```python
data = [
    ["Name", "Score"],
    ["Alice", 95],
    ["Bob", 88],
]
with open("scores.csv", "w") as f:
    for row in data:
        f.write(",".join(str(v) for v in row) + "\n")
```

---

## Key Takeaways
- `"w"` truncates the file — all previous content is lost
- `"a"` is safe for logs — never overwrites existing data
- Always add `\n` manually; `write()` doesn't add newlines automatically
- Use `csv` or `json` modules for structured data (covered in later days)

---

## Exercises
See `exercises.py`

---

<!-- nav -->
[📝 Exercises](https://github.com/nikunjjakhotia/Python-in-100-Days-course-hub/blob/main/Week04/Day25/exercises.py) | [← Day 24](../Day24/lesson.md) | [Day 26 →](../Day26/lesson.md)
<!-- nav -->
