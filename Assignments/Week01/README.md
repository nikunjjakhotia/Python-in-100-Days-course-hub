<!-- assignments-nav -->
[🏠 Home](../../) | [📚 Week 01 Lessons — Python Fundamentals](../../Week01/)

---
<!-- assignments-nav -->

# Week 1 Assignment — Personal Bio App

**Days 1–7 · Topics: Variables, Data Types, Strings, Lists, Dicts, Type Conversion**

Build a command-line app that collects information about the user and prints a neatly formatted bio card.

---

## 🎯 What You'll Build

A Python script that prompts the user for personal details and displays a polished bio card — like a business card in the terminal.

---

## 📋 Requirements

1. Ask the user for their **name**, **age**, **city**, **favourite programming language**, and **three hobbies** (collected one at a time and stored in a list).
2. Store each piece of information in an appropriately typed variable (string, int, list).
3. Calculate and display the **year they were born** using the current year minus their age.
4. Build a dictionary called `profile` that holds all collected data.
5. Print a formatted bio card using **f-strings** — no `+` string concatenation allowed.
6. If the user enters a non-numeric age, handle it gracefully and ask again (use a `while` loop + `isdigit()` or `try/except`).
7. Display the hobbies as a **numbered list** (1. …, 2. …, 3. …) using a `for` loop.
8. Add a closing section that prints the user's name in uppercase, lowercase, and title case.

---

## 💡 Hints

- `input()` always returns a string — cast to `int` with `int()` when you need a number.
- f-strings: `f"Hello, {name}!"` — the variable goes inside `{}`.
- `enumerate(hobbies, start=1)` gives `(1, hobby)` pairs — useful for numbered lists.
- Import `datetime` to get the current year: `datetime.date.today().year`.

---

## 📤 How to Submit

1. Save your solution as `Week01_assignment.py` inside this folder.
2. Run it end-to-end and confirm there are no errors.
3. Share a screenshot of the output on LinkedIn with **#Python100Days** and tag [@nikunjjakhotia](https://www.linkedin.com/in/nikunjjakhotia/).

---

## ✅ Marking Criteria

| Criterion | Marks |
|-----------|-------|
| All 5 inputs collected and stored correctly | /10 |
| Birth year calculated and displayed | /5 |
| `profile` dictionary built and populated | /10 |
| Bio card formatted with f-strings (no `+` concat) | /10 |
| Hobbies displayed as a numbered list via loop | /10 |
| Non-numeric age handled without crashing | /5 |
| **Total** | **/50** |
