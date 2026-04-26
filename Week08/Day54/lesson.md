# Day 54 – Error Handling with APIs

## Learning Objectives
- Handle connection errors, timeouts, and HTTP errors gracefully
- Implement retries with exponential back-off
- Write a robust `safe_get()` helper

---

## The requests Exception Hierarchy

```
requests.exceptions.RequestException        ← base
├── ConnectionError                          ← DNS / network failure
├── Timeout                                  ← request took too long
└── HTTPError                                ← 4xx / 5xx (from raise_for_status)
```

---

## Catching Errors

```python
import requests

def safe_get(url, **kwargs):
    try:
        r = requests.get(url, timeout=10, **kwargs)
        r.raise_for_status()
        return r.json()
    except requests.exceptions.Timeout:
        print(f"Timeout: {url}")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP {e.response.status_code}: {url}")
    except requests.exceptions.ConnectionError:
        print(f"Cannot connect to: {url}")
    return None

data = safe_get("https://jsonplaceholder.typicode.com/posts/1")
print(data)
```

---

## Retries with Exponential Back-off

```python
import time

def get_with_retry(url, retries=3, backoff=1.0):
    for attempt in range(1, retries + 1):
        try:
            r = requests.get(url, timeout=10)
            r.raise_for_status()
            return r.json()
        except requests.exceptions.RequestException as e:
            print(f"Attempt {attempt} failed: {e}")
            if attempt < retries:
                time.sleep(backoff * 2 ** (attempt - 1))
    return None
```

---

## Checking Status Without Raising

```python
r = requests.get("https://httpbin.org/status/404")
if r.status_code == 404:
    print("Resource not found")
elif r.ok:                      # True for 200–299
    print(r.json())
```

---

## Key Takeaways
- Always catch at least `RequestException` and `HTTPError`
- Use exponential back-off for retries — don't hammer a slow server
- `.ok` is `True` for any 2xx status code

---

## Exercises
See `exercises.py`
