# Day 10 – While Loops

## Learning Objectives
- Repeat code while a condition remains True
- Use `break` and `continue` to control loop flow
- Avoid infinite loops

---

## Core Concept

A `while` loop keeps running as long as its condition is `True`.

```python
count = 1
while count <= 5:
    print(f"Count: {count}")
    count += 1
```

---

## break — Exit the Loop Early

```python
while True:
    answer = input("Type 'quit' to exit: ")
    if answer == "quit":
        break
    print(f"You typed: {answer}")
```

---

## continue — Skip the Rest of This Iteration

```python
num = 0
while num < 10:
    num += 1
    if num % 2 == 0:
        continue        # skip even numbers
    print(num)          # prints only odd numbers
```

---

## Infinite Loop Warning

Always make sure the condition will eventually become `False`, or include a `break`. This loop runs forever:

```python
# DON'T DO THIS (without a break):
while True:
    print("Looping...")
```

---

## Common Pattern: Input Validation

```python
while True:
    age = int(input("Enter a positive age: "))
    if age > 0:
        break
    print("Age must be positive. Try again.")
print(f"Age accepted: {age}")
```

---

## Key Takeaways
- Use `while` when you don't know in advance how many iterations you need
- Always ensure the loop terminates
- `break` exits immediately; `continue` skips to the next iteration

---

## Exercises
See `exercises.py`
