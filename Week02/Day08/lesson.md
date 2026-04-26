# Day 08 – Conditional Statements: if / elif / else

## Learning Objectives
- Write decision-making code using `if`, `elif`, and `else`
- Use comparison and logical operators
- Understand how Python evaluates conditions

---

## Core Concept

Python uses indentation (4 spaces) to define code blocks inside conditions.

```python
age = 20

if age >= 18:
    print("Adult")
elif age >= 13:
    print("Teenager")
else:
    print("Child")
```

---

## Comparison Operators

| Operator | Meaning |
|---|---|
| `==` | Equal to |
| `!=` | Not equal |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal |
| `<=` | Less than or equal |

---

## Logical Operators

```python
# and — both conditions must be True
if age >= 18 and age <= 65:
    print("Working age")

# or — at least one must be True
if day == "Saturday" or day == "Sunday":
    print("Weekend!")

# not — reverses the condition
if not is_raining:
    print("Go for a walk")
```

---

## One-Line Conditional (Ternary)

```python
status = "Adult" if age >= 18 else "Minor"
print(status)
```

---

## Key Takeaways
- Only one branch in an `if/elif/else` chain executes
- Conditions evaluate to `True` or `False`
- Indentation is mandatory — Python will raise an error without it

---

## Exercises
See `exercises.py`
