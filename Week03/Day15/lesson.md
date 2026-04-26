# Day 15 – Defining Functions

## Learning Objectives
- Define and call reusable functions with `def`
- Understand why functions improve code organisation
- Use docstrings to document functions

---

## Core Concept

A function is a named, reusable block of code.

```python
def greet():
    print("Hello, Python learner!")

greet()   # Call the function
```

---

## Functions With Parameters

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")
greet("Bob")
```

---

## Default Parameter Values

```python
def greet(name="World"):
    print(f"Hello, {name}!")

greet()          # Hello, World!
greet("Nikunj")  # Hello, Nikunj!
```

---

## Docstrings

```python
def add(a, b):
    """Return the sum of a and b."""
    return a + b

help(add)        # Shows the docstring
```

---

## Why Functions?

| Without Functions | With Functions |
|---|---|
| Repeated code blocks | Write once, call many times |
| Hard to test | Easy to unit-test |
| Hard to read | Self-documenting names |

---

## Key Takeaways
- Name functions with verbs: `calculate_tax()`, `get_user()`, `print_report()`
- A function without `return` returns `None`
- Keep each function focused on one task (single responsibility)

---

## Exercises
See `exercises.py`
