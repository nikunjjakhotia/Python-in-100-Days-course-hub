<!-- nav -->
[← Day 32](../Day32/lesson.md) | [🏠 Home](../../) | [Day 34 →](../Day34/lesson.md)

---
<!-- nav -->

# Day 33 – Sorting & Filtering

## Learning Objectives
- Sort lists and complex structures with `sorted()` and `.sort()`
- Filter data with comprehensions and `filter()`
- Chain sorting and filtering for data pipelines

---

## sorted() vs .sort()

```python
nums = [3, 1, 4, 1, 5, 9, 2, 6]

sorted(nums)        # returns NEW sorted list; original unchanged
nums.sort()         # sorts IN-PLACE; returns None

sorted(nums, reverse=True)   # descending
```

---

## Sorting Complex Objects

```python
students = [
    {"name": "Charlie", "score": 71},
    {"name": "Alice",   "score": 95},
    {"name": "Bob",     "score": 82},
]

by_score = sorted(students, key=lambda s: s["score"], reverse=True)
for s in by_score:
    print(s["name"], s["score"])
```

---

## Multi-Key Sort

```python
data = [("Alice", 95), ("Bob", 95), ("Charlie", 88)]
sorted_data = sorted(data, key=lambda x: (-x[1], x[0]))
# Sort by score desc, then name asc on ties
```

---

## filter() vs Comprehension

```python
numbers = range(1, 21)

# filter()
evens = list(filter(lambda x: x % 2 == 0, numbers))

# Comprehension (more Pythonic)
evens = [x for x in numbers if x % 2 == 0]
```

---

## Key Takeaways
- Prefer comprehensions over `filter()` for readability
- `sorted()` is safe (non-destructive); `.sort()` modifies in place
- Negate the sort key to sort descending without `reverse=True` when combining multi-key sorts

---

## Exercises
See `exercises.py`

---

<!-- nav -->
[📝 Exercises](https://github.com/nikunjjakhotia/Python-in-100-Days-course-hub/blob/main/Week05/Day33/exercises.py) | [← Day 32](../Day32/lesson.md) | [Day 34 →](../Day34/lesson.md)
<!-- nav -->
