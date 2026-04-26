# Day 30 – Advanced Dictionaries

## Learning Objectives
- Use dictionary methods confidently
- Merge, copy, and update dictionaries
- Use `defaultdict` and `Counter` from `collections`

---

## Core Methods Recap

```python
d = {"a": 1, "b": 2, "c": 3}
d.get("x", 0)       # 0 (safe access)
d.keys()            # dict_keys
d.values()          # dict_values
d.items()           # dict_items — great for loops
d.pop("a")          # remove and return value
d.update({"d": 4})  # merge another dict in
```

---

## Merging Dicts (Python 3.9+)

```python
defaults = {"theme": "dark", "lang": "en"}
user_settings = {"theme": "light"}

merged = defaults | user_settings  # user_settings wins on conflicts
print(merged)  # {"theme": "light", "lang": "en"}
```

---

## defaultdict — No KeyError on Missing Keys

```python
from collections import defaultdict

word_count = defaultdict(int)
for word in "the cat sat on the mat the cat".split():
    word_count[word] += 1
print(dict(word_count))
```

---

## Counter — Count Occurrences

```python
from collections import Counter

votes = ["Alice", "Bob", "Alice", "Alice", "Bob", "Charlie"]
tally = Counter(votes)
print(tally)                  # Counter({'Alice': 3, 'Bob': 2, 'Charlie': 1})
print(tally.most_common(2))   # [('Alice', 3), ('Bob', 2)]
```

---

## Nested Dicts

```python
employees = {
    "alice": {"dept": "Engineering", "salary": 90000},
    "bob":   {"dept": "Marketing",   "salary": 75000},
}
print(employees["alice"]["dept"])  # Engineering
```

---

## Key Takeaways
- `defaultdict(int)` is the cleanest way to count items
- `Counter` is purpose-built for frequency analysis
- The `|` merge operator keeps the last value on key conflicts

---

## Exercises
See `exercises.py`
