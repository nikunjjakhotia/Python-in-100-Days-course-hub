# Day 19 – Lambda Functions

## Learning Objectives
- Write anonymous one-line functions with `lambda`
- Use `lambda` with `map()`, `filter()`, and `sorted()`
- Know when lambdas are appropriate (and when they're not)

---

## Syntax

```python
lambda arguments: expression
```

A lambda is just a compact function. These two are equivalent:

```python
def square(x):
    return x ** 2

square = lambda x: x ** 2
```

---

## Lambda with map()

`map()` applies a function to every item in an iterable.

```python
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)   # [1, 4, 9, 16, 25]
```

---

## Lambda with filter()

`filter()` keeps only items where the function returns `True`.

```python
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, numbers))
print(evens)   # [2, 4, 6]
```

---

## Lambda with sorted()

Sort by a custom key without defining a full function.

```python
students = [("Alice", 88), ("Bob", 95), ("Charlie", 72)]
by_score = sorted(students, key=lambda s: s[1], reverse=True)
print(by_score)
```

---

## When NOT to Use Lambda

- Multi-line logic → use a regular `def`
- Code that needs a docstring
- Anywhere readability suffers

---

## Key Takeaways
- Lambda is best for short, one-off functions passed to `map/filter/sorted`
- Always ask: "Is a named function clearer here?"
- Python style guides (PEP 8) discourage assigning lambdas to variables

---

## Exercises
See `exercises.py`
