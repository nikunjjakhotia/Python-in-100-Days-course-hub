<!-- nav -->
[← Day 28](../../Week04/Day28/lesson.md) | [🏠 Home](../../) | [Day 30 →](../Day30/lesson.md)

---
<!-- nav -->

# Day 29 – List Comprehensions

## Learning Objectives
- Write concise list-building code with list comprehensions
- Add conditions to filter items inline
- Understand when comprehensions improve or hurt readability

---

## Syntax

```python
[expression for item in iterable if condition]
```

---

## Basic Comprehension

```python
# Traditional loop
squares = []
for x in range(1, 6):
    squares.append(x ** 2)

# Comprehension
squares = [x ** 2 for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]
```

---

## With a Filter Condition

```python
evens = [x for x in range(20) if x % 2 == 0]
print(evens)  # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```

---

## String Comprehension

```python
sentence = "Hello World Python"
upper_words = [word.upper() for word in sentence.split()]
print(upper_words)
```

---

## Nested Comprehension

```python
matrix = [[i * j for j in range(1, 4)] for i in range(1, 4)]
for row in matrix:
    print(row)
```

---

## Dict and Set Comprehensions

```python
# Dict comprehension
squares_dict = {x: x**2 for x in range(1, 6)}

# Set comprehension
unique_lengths = {len(w) for w in ["cat", "dog", "elephant", "ant"]}
```

---

## Key Takeaways
- Comprehensions are faster than equivalent `for` loops with `.append()`
- Keep them to one line — if it needs multiple lines, use a regular loop
- Avoid nesting more than two levels deep

---

## Exercises
See `exercises.py`

---

<!-- nav -->
[📝 Exercises](https://github.com/nikunjjakhotia/Python-in-100-Days-course-hub/blob/main/Week05/Day29/exercises.py) | [← Day 28](../../Week04/Day28/lesson.md) | [Day 30 →](../Day30/lesson.md)
<!-- nav -->
