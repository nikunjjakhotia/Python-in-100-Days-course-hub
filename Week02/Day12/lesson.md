<!-- nav -->
[← Day 11](../Day11/lesson.md) | [🏠 Home](../../) | [Day 13 →](../Day13/lesson.md)

---
<!-- nav -->

# Day 12 – range() & Loop Control

## Learning Objectives
- Master `range()` with start, stop, and step
- Use `break`, `continue`, and `else` with loops
- Write nested loops

---

## range() Deep Dive

```python
range(stop)           # 0 to stop-1
range(start, stop)    # start to stop-1
range(start, stop, step)  # with custom step

# Count down
for i in range(10, 0, -1):
    print(i)
```

---

## Loop else Clause

The `else` block runs only if the loop completed without hitting `break`.

```python
for n in range(2, 10):
    for factor in range(2, n):
        if n % factor == 0:
            break
    else:
        print(f"{n} is prime")
```

---

## Nested Loops

```python
for row in range(1, 4):
    for col in range(1, 4):
        print(f"({row},{col})", end=" ")
    print()
```

Output:
```
(1,1) (1,2) (1,3)
(2,1) (2,2) (2,3)
(3,1) (3,2) (3,3)
```

---

## Multiplication Table Pattern

```python
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i * j:3}", end="")
    print()
```

---

## Key Takeaways
- `range(start, stop, step)` is very flexible
- Negative step counts down
- `for...else` is a unique Python feature — the `else` runs if no `break` occurred

---

## Exercises
See `exercises.py`

---

<!-- nav -->
[📝 Exercises](https://github.com/nikunjjakhotia/Python-in-100-Days-course-hub/blob/main/Week02/Day12/exercises.py) | [🏠 Home](/Python-in-100-Days-course-hub/) | [← Day 11](../Day11/lesson.md) | [Day 13 →](../Day13/lesson.md)
<!-- nav -->
