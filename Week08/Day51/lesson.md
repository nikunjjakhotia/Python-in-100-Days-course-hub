<!-- nav -->
[← Day 50](../Day50/lesson.md) | [🏠 Home](../../) | [Day 52 →](../Day52/lesson.md)

---
<!-- nav -->

# Day 51 – GET Requests & Query Parameters

## Learning Objectives
- Send GET requests with query parameters
- Inspect headers and response metadata
- Handle non-JSON responses

---

## Query Parameters

Query parameters appear after `?` in a URL: `/search?q=python&page=2`

Pass them as a `params` dict — `requests` URL-encodes them automatically:

```python
import requests

r = requests.get(
    "https://httpbin.org/get",
    params={"q": "python", "page": 2}
)
print(r.url)   # https://httpbin.org/get?q=python&page=2
print(r.json())
```

---

## Request Headers

Send custom headers (e.g. a User-Agent or Accept type) via the `headers` dict:

```python
r = requests.get(
    "https://httpbin.org/headers",
    headers={"User-Agent": "MyApp/1.0", "Accept": "application/json"}
)
print(r.json())
```

---

## Timeout

Always set a timeout so your program doesn't hang forever:

```python
try:
    r = requests.get("https://httpbin.org/delay/3", timeout=5)
    r.raise_for_status()
    print(r.json())
except requests.exceptions.Timeout:
    print("Request timed out")
except requests.exceptions.HTTPError as e:
    print(f"HTTP error: {e}")
```

---

## Working with Non-JSON Responses

```python
r = requests.get("https://httpbin.org/image/png")
with open("image.png", "wb") as f:
    f.write(r.content)   # r.content is raw bytes
```

---

## Key Takeaways
- Use `params={}` for query strings — never build URLs manually with `+`
- Always pass `timeout=` so requests can't hang
- Use `.content` for binary data, `.text` for strings, `.json()` for JSON

---

## Exercises
See `exercises.py`

---

<!-- nav -->
[📝 Exercises](https://github.com/nikunjjakhotia/Python-in-100-Days-course-hub/blob/main/Week08/Day51/exercises.py) | [🏠 Home](/Python-in-100-Days-course-hub/) | [← Day 50](../Day50/lesson.md) | [Day 52 →](../Day52/lesson.md)
<!-- nav -->
