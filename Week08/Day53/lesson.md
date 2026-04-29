<!-- nav -->
[← Day 52](../Day52/lesson.md) | [🏠 Home](../../) | [Day 54 →](../Day54/lesson.md)

---
<!-- nav -->

# Day 53 – POST Requests & Authentication

## Learning Objectives
- Send POST requests with JSON bodies
- Use API key and Bearer token authentication
- Read credentials safely from environment variables

---

## POST Requests

Use POST to **create** resources. Pass data as JSON:

```python
import requests

payload = {"title": "My Post", "body": "Hello!", "userId": 1}
r = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=payload          # sets Content-Type: application/json automatically
)
r.raise_for_status()
print(r.status_code)   # 201
print(r.json())
```

`json=` serialises the dict; `data=` sends form-encoded data.

---

## API Key Authentication

Many APIs require a key in a header or query parameter:

```python
# In a header (most common):
r = requests.get(
    "https://api.example.com/data",
    headers={"X-API-Key": "your_key_here"}
)

# As a query param (some APIs):
r = requests.get(
    "https://api.example.com/data",
    params={"api_key": "your_key_here"}
)
```

---

## Bearer Token (OAuth / JWT)

```python
token = "eyJhbGci..."
r = requests.get(
    "https://api.example.com/me",
    headers={"Authorization": f"Bearer {token}"}
)
```

---

## Store Secrets in `.env`, Never in Code

```bash
# .env
API_KEY=abc123secret
```

```python
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("API_KEY")
```

Add `.env` to `.gitignore` so it never gets committed.

---

## Key Takeaways
- `json=` in `requests.post()` sets the body and content-type in one step
- Never hardcode API keys — load them from environment variables
- Bearer token goes in `Authorization: Bearer <token>` header

---

## Exercises
See `exercises.py`

---

<!-- nav -->
[📝 Exercises](https://github.com/nikunjjakhotia/Python-in-100-Days-course-hub/blob/main/Week08/Day53/exercises.py) | [🏠 Home](/Python-in-100-Days-course-hub/) | [← Day 52](../Day52/lesson.md) | [Day 54 →](../Day54/lesson.md)
<!-- nav -->
