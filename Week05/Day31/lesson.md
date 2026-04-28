<!-- nav -->
[← Day 30](../Day30/lesson.md) | [🏠 Home](../../) | [Day 32 →](../Day32/lesson.md)

---
<!-- nav -->

# Day 31 – Sets & Operations

## Learning Objectives
- Use sets for deduplication and membership testing
- Perform set algebra: union, intersection, difference, symmetric difference
- Know when to choose a set over a list

---

## Creating Sets

```python
fruits = {"apple", "banana", "cherry"}
empty = set()          # NOT {} — that creates a dict!
from_list = set([1, 2, 2, 3, 3, 3])  # {1, 2, 3}
```

---

## Set Operations

```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

a | b    # Union:                {1, 2, 3, 4, 5, 6}
a & b    # Intersection:         {3, 4}
a - b    # Difference (in a, not b): {1, 2}
a ^ b    # Symmetric difference:  {1, 2, 5, 6}
```

---

## Membership Testing

Sets use hash lookups — O(1) vs O(n) for lists.

```python
allowed_users = {"alice", "bob", "charlie"}
user = "dave"
if user in allowed_users:
    print("Access granted")
else:
    print("Access denied")
```

---

## Subset / Superset Checks

```python
{1, 2}.issubset({1, 2, 3})      # True
{1, 2, 3}.issuperset({1, 2})    # True
{1, 2}.isdisjoint({3, 4})       # True (no common elements)
```

---

## Frozenset — Immutable Set

```python
fs = frozenset({1, 2, 3})
# fs.add(4)  # AttributeError — can't modify
```

---

## Key Takeaways
- Sets automatically remove duplicates
- `in` checks are O(1) for sets — great for large allowed-lists
- Sets are unordered — don't rely on insertion order

---

## Exercises
See `exercises.py`

---

<!-- nav -->
[📝 Exercises](exercises.py) | [← Day 30](../Day30/lesson.md) | [Day 32 →](../Day32/lesson.md)
<!-- nav -->
