<!-- nav -->
[← Day 49](../../Week07/Day49/lesson.md) | [🏠 Home](../../) | [Day 51 →](../Day51/lesson.md)

---
<!-- nav -->

# Day 50 – Intro to APIs

## Learning Objectives
- Understand what an API is and how HTTP works
- Know the difference between REST and other API styles
- Make your first request with the `requests` library

---

## What Is an API?

An **Application Programming Interface (API)** is a contract that lets two programs talk to each other. A **Web API** uses HTTP — the same protocol your browser uses — to exchange data (usually JSON).

```
Client                     Server
  │── GET /weather?city=NYC ──▶│
  │◀── 200 OK  { "temp": 72 } ─│
```

---

## HTTP Methods

| Method | Purpose |
|--------|---------|
| `GET` | Read data |
| `POST` | Create new data |
| `PUT` / `PATCH` | Update data |
| `DELETE` | Remove data |

---

## HTTP Status Codes

| Code | Meaning |
|------|---------|
| 200 | OK |
| 201 | Created |
| 400 | Bad Request |
| 401 | Unauthorised |
| 404 | Not Found |
| 500 | Server Error |

---

## REST

**REST (Representational State Transfer)** is the most common web API style:
- Resources are nouns: `/users`, `/posts/42`
- HTTP method expresses the action
- Stateless — each request is self-contained

---

## The `requests` Library

```bash
pip install requests
```

```python
import requests

response = requests.get("https://httpbin.org/get")
print(response.status_code)   # 200
print(response.json())        # parsed JSON as a dict
```

---

## Anatomy of a Response

```python
r = requests.get("https://httpbin.org/get")
r.status_code    # int — HTTP status
r.headers        # dict — response headers
r.text           # raw body as string
r.json()         # body parsed as Python dict/list
r.raise_for_status()  # raises HTTPError if 4xx/5xx
```

---

## Key Takeaways
- An API is a contract for two programs to communicate over HTTP
- REST APIs use URLs as nouns and HTTP methods as verbs
- `requests` makes HTTP calls simple; always call `.raise_for_status()` to catch errors early

---

## Exercises
See `exercises.py`

---

<!-- nav -->
[📝 Exercises](exercises.py) | [← Day 49](../../Week07/Day49/lesson.md) | [Day 51 →](../Day51/lesson.md)
<!-- nav -->
