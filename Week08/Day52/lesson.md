<!-- nav -->
[← Day 51](../Day51/lesson.md) | [🏠 Home](../../) | [Day 53 →](../Day53/lesson.md)

---
<!-- nav -->

# Day 52 – JSON Parsing & Response Handling

## Learning Objectives
- Parse and navigate nested JSON responses
- Use list comprehensions to extract fields
- Write helper functions to flatten API data

---

## JSON ↔ Python

| JSON | Python |
|------|--------|
| object `{}` | `dict` |
| array `[]` | `list` |
| string `""` | `str` |
| number | `int` or `float` |
| `true`/`false` | `True`/`False` |
| `null` | `None` |

---

## Parsing a Nested Response

```python
import requests

r = requests.get("https://jsonplaceholder.typicode.com/users")
users = r.json()   # list of dicts

for user in users[:3]:
    print(user["name"], user["email"])
    print("City:", user["address"]["city"])
```

---

## Extracting with List Comprehensions

```python
names  = [u["name"]  for u in users]
emails = [u["email"] for u in users if "example" not in u["email"]]
print(names)
```

---

## Safe Access with `.get()`

When a key might be missing:

```python
for user in users:
    phone = user.get("phone", "N/A")
    company = user.get("company", {}).get("name", "N/A")
    print(f"{user['name']} | {phone} | {company}")
```

---

## Writing to a JSON File

```python
import json

with open("users.json", "w") as f:
    json.dump(users, f, indent=2)

with open("users.json") as f:
    loaded = json.load(f)
print(loaded[0]["name"])
```

---

## Key Takeaways
- `.json()` converts the response body into Python dicts/lists
- Use `.get(key, default)` for optional fields — never crash on missing keys
- `json.dump` / `json.load` let you persist API data to disk

---

## Exercises
See `exercises.py`

---

<!-- nav -->
[📝 Exercises](https://github.com/nikunjjakhotia/Python-in-100-Days-course-hub/blob/main/Week08/Day52/exercises.py) | [← Day 51](../Day51/lesson.md) | [Day 53 →](../Day53/lesson.md)
<!-- nav -->
