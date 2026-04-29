<!-- nav -->
[← Day 31](../Day31/lesson.md) | [🏠 Home](../../) | [Day 33 →](../Day33/lesson.md)

---
<!-- nav -->

# Day 32 – Nested Data Structures

## Learning Objectives
- Work with lists of dictionaries and dicts of lists
- Access and update nested data
- Iterate through complex structures

---

## List of Dictionaries

The most common pattern for tabular data.

```python
students = [
    {"name": "Alice", "grade": "A", "score": 95},
    {"name": "Bob",   "grade": "B", "score": 82},
    {"name": "Charlie", "grade": "C", "score": 71},
]

for s in students:
    print(f"{s['name']}: {s['score']}")
```

---

## Dict of Lists

Great for grouping related items.

```python
schedule = {
    "Monday":    ["Math", "English"],
    "Tuesday":   ["Science", "Art"],
    "Wednesday": ["Math", "PE", "History"],
}

for day, classes in schedule.items():
    print(f"{day}: {', '.join(classes)}")
```

---

## Deep Access

```python
company = {
    "engineering": {
        "team_size": 15,
        "lead": "Alice",
        "tools": ["Python", "Docker", "Kubernetes"]
    }
}

print(company["engineering"]["lead"])        # Alice
print(company["engineering"]["tools"][0])    # Python
```

---

## Updating Nested Data

```python
students[0]["score"] = 98     # update
students.append({"name": "Diana", "grade": "A+", "score": 100})
```

---

## Key Takeaways
- `list[i]["key"]` and `dict["key"][i]` are the access patterns
- Always check key existence with `.get()` when the data is uncertain
- JSON data is almost always nested dicts/lists — this is exactly how APIs return data

---

## Exercises
See `exercises.py`

---

<!-- nav -->
[📝 Exercises](https://github.com/nikunjjakhotia/Python-in-100-Days-course-hub/blob/main/Week05/Day32/exercises.py) | [🏠 Home](/Python-in-100-Days-course-hub/) | [← Day 31](../Day31/lesson.md) | [Day 33 →](../Day33/lesson.md)
<!-- nav -->
