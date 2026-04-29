<!-- nav -->
[← Day 16](../Day16/lesson.md) | [🏠 Home](../../) | [Day 18 →](../Day18/lesson.md)

---
<!-- nav -->

# Day 17 – Scope: Local, Global & Enclosing

## Learning Objectives
- Understand where variables live (scope)
- Distinguish local vs global variables
- Use the `global` and `nonlocal` keywords carefully

---

## Local Scope

Variables created inside a function only exist inside it.

```python
def greet():
    message = "Hello!"   # local variable
    print(message)

greet()
# print(message)  # NameError — message doesn't exist here
```

---

## Global Scope

Variables defined at the top level of a script are global.

```python
name = "Nikunj"  # global

def show_name():
    print(name)  # can READ global variables

show_name()
```

---

## Modifying a Global Variable

```python
counter = 0

def increment():
    global counter    # declare intent to modify
    counter += 1

increment()
increment()
print(counter)  # 2
```

> Best practice: avoid modifying globals. Return values instead.

---

## Enclosing Scope (Closure) + nonlocal

```python
def outer():
    count = 0
    def inner():
        nonlocal count
        count += 1
        print(count)
    inner()
    inner()

outer()   # prints 1, then 2
```

---

## LEGB Rule (Python's lookup order)

| Letter | Scope |
|---|---|
| L | Local (inside current function) |
| E | Enclosing (outer function) |
| G | Global (module level) |
| B | Built-in (Python builtins) |

---

## Key Takeaways
- Prefer returning values over using `global`
- `global` and `nonlocal` exist for edge cases, not everyday use
- Name collisions between local and global variables are a common bug source

---

## Exercises
See `exercises.py`

---

<!-- nav -->
[📝 Exercises](https://github.com/nikunjjakhotia/Python-in-100-Days-course-hub/blob/main/Week03/Day17/exercises.py) | [🏠 Home](/Python-in-100-Days-course-hub/) | [← Day 16](../Day16/lesson.md) | [Day 18 →](../Day18/lesson.md)
<!-- nav -->
