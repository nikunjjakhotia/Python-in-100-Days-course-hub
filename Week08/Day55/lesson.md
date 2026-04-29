<!-- nav -->
[← Day 54](../Day54/lesson.md) | [🏠 Home](../../) | [Day 56 →](../Day56/lesson.md)

---
<!-- nav -->

# Day 55 – Pagination & Rate Limiting

## Learning Objectives
- Retrieve all pages from a paginated API
- Respect rate limits with delays
- Use a `Session` object for connection reuse

---

## What Is Pagination?

APIs return data in pages to avoid huge payloads.  
Common patterns:

```
# Offset / limit
GET /posts?page=1&per_page=10
GET /posts?offset=0&limit=10

# Cursor
GET /items?cursor=abc123
```

---

## Fetching All Pages

```python
import requests

def fetch_all_pages(base_url, per_page=10):
    results = []
    page = 1
    while True:
        r = requests.get(base_url, params={"_page": page, "_limit": per_page}, timeout=10)
        r.raise_for_status()
        data = r.json()
        if not data:          # empty page → we're done
            break
        results.extend(data)
        page += 1
    return results

posts = fetch_all_pages("https://jsonplaceholder.typicode.com/posts")
print(f"Total posts: {len(posts)}")
```

---

## Rate Limiting

Many APIs restrict how many requests you can make per minute/hour.

```python
import time

for page in range(1, 6):
    r = requests.get(f"https://httpbin.org/get", params={"page": page}, timeout=10)
    print(f"Page {page}: {r.status_code}")
    time.sleep(0.5)   # 500 ms between requests
```

Check response headers for rate limit info:
```python
print(r.headers.get("X-RateLimit-Remaining"))
print(r.headers.get("X-RateLimit-Reset"))
```

---

## `requests.Session`

Reusing a `Session` keeps HTTP connections alive (connection pooling) and lets you set default headers once:

```python
session = requests.Session()
session.headers.update({"Authorization": "Bearer mytoken"})

for i in range(1, 4):
    r = session.get(f"https://jsonplaceholder.typicode.com/posts/{i}", timeout=10)
    print(r.json()["title"])
```

---

## Key Takeaways
- Stop pagination when the API returns an empty page or a `next: null` link
- Add small `time.sleep()` delays between requests to respect rate limits
- Use `Session` when making many requests to the same host

---

## Exercises
See `exercises.py`

---

<!-- nav -->
[📝 Exercises](https://github.com/nikunjjakhotia/Python-in-100-Days-course-hub/blob/main/Week08/Day55/exercises.py) | [🏠 Home](/Python-in-100-Days-course-hub/) | [← Day 54](../Day54/lesson.md) | [Day 56 →](../Day56/lesson.md)
<!-- nav -->
