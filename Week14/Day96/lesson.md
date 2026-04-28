<!-- nav -->
[← Day 95](../Day95/lesson.md) | [🏠 Home](../../) | [Day 97 →](../Day97/lesson.md)

---
<!-- nav -->

# Day 96 – Interview Prep: Data Structures

## Learning Objectives
- Know Python's built-in data structures and their time complexities
- Solve common data structure interview problems
- Recognise which structure to reach for in which situation

---

## Big-O Quick Reference

| Operation | list | dict | set | deque |
|-----------|------|------|-----|-------|
| Access by index | O(1) | — | — | O(n) |
| Insert/delete at end | O(1) | — | — | O(1) |
| Insert/delete at front | O(n) | — | — | O(1) |
| Search (in) | O(n) | O(1) | O(1) | O(n) |
| Insert | O(1)† | O(1) | O(1) | O(1) |

†amortised

---

## Common Patterns

### Two-pointer
```python
def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        complement = target - n
        if complement in seen:
            return [seen[complement], i]
        seen[n] = i
```

### Sliding window
```python
def max_subarray_sum(nums, k):
    window = sum(nums[:k])
    best   = window
    for i in range(k, len(nums)):
        window += nums[i] - nums[i - k]
        best = max(best, window)
    return best
```

### Stack for bracket matching
```python
def is_valid(s):
    stack  = []
    pairs  = {")": "(", "}": "{", "]": "["}
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
    return not stack
```

---

## Key Takeaways
- `dict` and `set` lookups are O(1) — use them to replace O(n) list searches
- `collections.deque` for queues — O(1) append/pop from both ends
- Recognise two-pointer, sliding window, and stack patterns — they cover 80% of array/string problems

---

## Exercises
See `exercises.py`

---

<!-- nav -->
[📝 Exercises](exercises.py) | [← Day 95](../Day95/lesson.md) | [Day 97 →](../Day97/lesson.md)
<!-- nav -->
