# Day 11 – For Loops

## Learning Objectives
- Iterate over sequences with `for`
- Loop through strings, lists, and ranges
- Use `enumerate()` and `zip()`

---

## Core Concept

A `for` loop iterates over any iterable (list, string, range, etc.).

```python
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
```

---

## Looping Over a String

```python
for char in "Python":
    print(char)
```

---

## Using range()

```python
for i in range(5):        # 0, 1, 2, 3, 4
    print(i)

for i in range(1, 6):     # 1, 2, 3, 4, 5
    print(i)

for i in range(0, 10, 2): # 0, 2, 4, 6, 8 (step 2)
    print(i)
```

---

## enumerate() — Index + Value Together

```python
names = ["Alice", "Bob", "Charlie"]
for index, name in enumerate(names):
    print(f"{index + 1}. {name}")
```

---

## zip() — Loop Over Two Lists in Parallel

```python
names = ["Alice", "Bob"]
scores = [95, 88]
for name, score in zip(names, scores):
    print(f"{name}: {score}")
```

---

## Key Takeaways
- `for` is best when the number of iterations is known
- `enumerate()` avoids manually tracking an index counter
- `zip()` combines two iterables element-by-element

---

## Exercises
See `exercises.py`
