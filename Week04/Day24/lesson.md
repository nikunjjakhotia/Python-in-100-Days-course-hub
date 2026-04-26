# Day 24 – Reading Files

## Learning Objectives
- Open and read text files with `open()`
- Use context managers (`with`) for safe file handling
- Read files line by line and as full text

---

## Opening a File

```python
f = open("data.txt", "r")   # "r" = read mode
content = f.read()
f.close()                   # always close!
```

---

## The Better Way: Context Manager

The `with` statement closes the file automatically, even if an error occurs.

```python
with open("data.txt", "r") as f:
    content = f.read()
print(content)
```

---

## Reading Methods

```python
# Read entire file as one string
content = f.read()

# Read one line at a time
line = f.readline()

# Read all lines into a list
lines = f.readlines()

# Iterate line by line (memory-efficient for large files)
for line in f:
    print(line.strip())
```

---

## Common File Modes

| Mode | Description |
|---|---|
| `"r"` | Read (default) |
| `"w"` | Write (overwrites) |
| `"a"` | Append |
| `"r+"` | Read and write |

---

## Handling FileNotFoundError

```python
try:
    with open("missing.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("File does not exist.")
```

---

## Key Takeaways
- Always use `with open(...)` — it guarantees the file is closed
- `strip()` removes trailing `\n` when iterating lines
- Use relative paths for portability; `os.path` helps build cross-platform paths

---

## Exercises
See `exercises.py`
