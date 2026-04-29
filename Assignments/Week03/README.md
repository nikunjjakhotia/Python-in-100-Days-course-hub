<!-- assignments-nav -->
[🏠 Home](../../) | [📚 Week 03 Lessons — Functions](../../Week03/)

---
<!-- assignments-nav -->

# Week 3 Assignment — Calculator & Unit Converter

**Days 15–21 · Topics: Functions, Parameters, \*args/\*\*kwargs, Scope, Lambda, Recursion**

Build a CLI toolkit with two tools — a scientific calculator with history and a unit converter — navigated from a single menu.

---

## 🎯 What You'll Build

A well-structured Python program split into clean functions, where each tool is self-contained and the main menu ties everything together.

---

## 📋 Requirements

1. **Calculator:** a `calculate(a, b, op)` function supporting `+`, `-`, `*`, `/`, `%`, and `**`; raise `ValueError` for division by zero and unsupported operators.
2. **History:** store the last 10 results in a module-level list; display them with `show_history()`.
3. **Recursive power:** implement `power(base, exp)` recursively and use it inside the calculator for the `**` operation.
4. **Unit converter:** write separate functions for length (`km ↔ miles`), weight (`kg ↔ lbs`), and temperature (`°C ↔ °F`); use default parameters where sensible.
5. **Lambda sorting:** after each converter call, use a `lambda` with `sorted()` to display all conversion results in ascending order of output value.
6. **`*args` function:** write `bulk_convert(*values, unit_from, unit_to)` that converts any number of values in one call.
7. **`main()` menu:** a `while True` loop with options `1) Calculator  2) Unit Converter  3) History  4) Quit`.
8. Keep all functions in a module called `toolkit.py` and import them into `Week03_assignment.py` — do not put logic in the global scope.

---

## 💡 Hints

- Recursion base case: `if exp == 0: return 1`.
- `round(result, 4)` keeps output readable.
- Use `global history` or pass history as a parameter — document which approach you chose and why.
- Temperature formula: `°F = °C × 9/5 + 32`.

---

## 📤 How to Submit

1. Save your solution as `Week03_assignment.py` (plus `toolkit.py`) inside this folder.
2. Demo both tools and history from the menu with no errors.
3. Share a screenshot on LinkedIn with **#Python100Days** and tag [@nikunjjakhotia](https://www.linkedin.com/in/nikunjjakhotia/).

---

## ✅ Marking Criteria

| Criterion | Marks |
|-----------|-------|
| Calculator handles all 6 operators + error cases | /10 |
| History stored and displayed correctly | /5 |
| Recursive `power()` used for `**` | /10 |
| Unit converter covers length, weight, temperature | /10 |
| `*args` bulk converter works for multiple values | /10 |
| `main()` menu loops correctly and quits cleanly | /5 |
| **Total** | **/50** |
