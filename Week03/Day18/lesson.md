# Day 18 – Recursion

## Learning Objectives
- Understand what recursion is and when to use it
- Identify the base case and recursive case
- Avoid infinite recursion with proper base cases

---

## What Is Recursion?

A function that calls itself is recursive. Every recursive function needs:
1. **Base case** — the condition that stops the recursion
2. **Recursive case** — the function calling itself with a smaller input

```python
def countdown(n):
    if n <= 0:       # base case
        print("Go!")
        return
    print(n)
    countdown(n - 1) # recursive case

countdown(5)
```

---

## Classic Example: Factorial

```python
def factorial(n):
    if n == 0:          # base case
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # 120  (5 × 4 × 3 × 2 × 1)
```

---

## Fibonacci Sequence

```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(8):
    print(fibonacci(i), end=" ")  # 0 1 1 2 3 5 8 13
```

---

## Recursion vs Iteration

| Recursion | Iteration |
|---|---|
| Elegant for tree/nested structures | Faster and uses less memory |
| Risk of stack overflow on deep calls | Safe for large inputs |

---

## Key Takeaways
- Always define a base case — recursion without one causes a `RecursionError`
- Python's default recursion limit is 1000 calls
- Fibonacci computed recursively is exponential — iteration or memoization is better for large n

---

## Exercises
See `exercises.py`
