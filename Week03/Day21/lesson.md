<!-- nav -->
[← Day 20](../Day20/lesson.md) | [🏠 Home](../../) | [Day 22 →](../../Week04/Day22/lesson.md)

---
<!-- nav -->

# Day 21 – Project: Calculator App

## What You're Building
A menu-driven command-line calculator that supports basic and advanced operations. Users interact through a loop until they choose to exit.

---

## Learning Objectives
- Organise code into small, focused functions
- Use a `while True` loop for a persistent menu
- Handle division by zero gracefully

---

## Project Spec

### Operations to support:
| Option | Operation |
|---|---|
| 1 | Addition |
| 2 | Subtraction |
| 3 | Multiplication |
| 4 | Division |
| 5 | Power (a^b) |
| 6 | Square root |
| 7 | Exit |

### Sample Output:
```
=== PYTHON CALCULATOR ===
1. Add       2. Subtract
3. Multiply  4. Divide
5. Power     6. Square Root
7. Exit

Choose an option: 1
Enter first number: 15
Enter second number: 7
Result: 15 + 7 = 22
```

---

## Skills Used
- Functions with parameters and return values
- `while` loop menu
- `if/elif/else`
- Exception handling (division by zero)
- `math.sqrt()`

---

## Starter Code
See `exercises.py` for the full project.

---

## Bonus Challenges
1. Add modulus (`%`) operation
2. Keep a history list of all calculations
3. Let the user use the previous result as the next input

---

<!-- nav -->
[📝 Exercises](https://github.com/nikunjjakhotia/Python-in-100-Days-course-hub/blob/main/Week03/Day21/exercises.py) | [← Day 20](../Day20/lesson.md) | [Day 22 →](../../Week04/Day22/lesson.md)
<!-- nav -->
