<!-- nav -->
[← Day 96](../Day96/lesson.md) | [🏠 Home](../../) | [Day 98 →](../Day98/lesson.md)

---
<!-- nav -->

# Day 97 – Interview Prep: Algorithms

## Learning Objectives
- Implement and explain sorting algorithms
- Understand recursion and memoisation
- Solve common algorithm interview problems

---

## Sorting

```python
# Built-in — always use this in production
nums.sort()                        # in-place
sorted_nums = sorted(nums)         # new list

# Sort by key
people.sort(key=lambda p: p["age"])
words.sort(key=len, reverse=True)
```

---

## Binary Search

O(log n) — only works on a sorted list.

```python
def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1
```

---

## Recursion

```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)
```

---

## Memoisation

Cache results to avoid recomputation:

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(100))   # instant
```

---

## Greedy / Common Patterns

```python
# Reverse a string
s[::-1]

# Check palindrome
s == s[::-1]

# Count chars
from collections import Counter
Counter("hello")   # Counter({'l': 2, 'h': 1, 'e': 1, 'o': 1})

# Flatten a nested list
flat = [x for sub in nested for x in sub]
```

---

## Key Takeaways
- Know binary search — it comes up in almost every interview
- `@lru_cache` turns naive recursion into O(n) memoised recursion in one line
- Practice explaining your thought process aloud — that's what interviewers evaluate

---

## Exercises
See `exercises.py`

---

<!-- nav -->
[📝 Exercises](https://github.com/nikunjjakhotia/Python-in-100-Days-course-hub/blob/main/Week14/Day97/exercises.py) | [← Day 96](../Day96/lesson.md) | [Day 98 →](../Day98/lesson.md)
<!-- nav -->
