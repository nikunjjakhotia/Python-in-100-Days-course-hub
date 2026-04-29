<!-- nav -->
[← Day 08](../Day08/lesson.md) | [🏠 Home](../../) | [Day 10 →](../Day10/lesson.md)

---
<!-- nav -->

# Day 09 – Nested Conditions

## Learning Objectives
- Write conditions inside other conditions
- Understand when to use nested `if` vs `elif`
- Avoid deeply nested code with logical operators

---

## Core Concept

Nested conditions allow fine-grained decisions — check a broad condition first, then narrow down.

```python
is_logged_in = True
is_admin = False

if is_logged_in:
    if is_admin:
        print("Welcome, Admin!")
    else:
        print("Welcome, User!")
else:
    print("Please log in.")
```

---

## When to Flatten with `and` / `or`

Deeply nested code is hard to read. Often a logical operator does the same job more cleanly:

```python
# Nested version
if temperature > 25:
    if humidity < 60:
        print("Great day for a run!")

# Flat version (preferred)
if temperature > 25 and humidity < 60:
    print("Great day for a run!")
```

---

## Real-World Example: Ticket Pricing

```python
age = int(input("Age: "))
is_member = input("Member? (yes/no): ").lower() == "yes"

if age < 12:
    price = 5
elif age >= 65:
    price = 7
else:
    if is_member:
        price = 10
    else:
        price = 15

print(f"Your ticket price: ${price}")
```

---

## Key Takeaways
- Nest only when the inner condition only makes sense after the outer passes
- Prefer flat logic with `and`/`or` when possible
- Never go more than 2–3 levels deep without refactoring

---

## Exercises
See `exercises.py`

---

<!-- nav -->
[📝 Exercises](https://github.com/nikunjjakhotia/Python-in-100-Days-course-hub/blob/main/Week02/Day09/exercises.py) | [← Day 08](../Day08/lesson.md) | [Day 10 →](../Day10/lesson.md)
<!-- nav -->
