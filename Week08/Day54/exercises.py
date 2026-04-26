# Day 54 – Error Handling with APIs

import requests, time

# Exercise 1: Write safe_get(url) that catches Timeout, HTTPError, and ConnectionError.
# Test it against /status/200, /status/404, and a bad domain.

# Solution:
def safe_get(url, **kwargs):
    try:
        r = requests.get(url, timeout=8, **kwargs)
        r.raise_for_status()
        return r
    except requests.exceptions.Timeout:
        print(f"[Timeout] {url}")
    except requests.exceptions.HTTPError as e:
        print(f"[HTTP {e.response.status_code}] {url}")
    except requests.exceptions.ConnectionError:
        print(f"[No connection] {url}")
    return None

safe_get("https://httpbin.org/status/200")
safe_get("https://httpbin.org/status/500")
safe_get("https://this-domain-does-not-exist-xyz.com")


# Exercise 2: Implement get_with_retry(url, retries=3, backoff=0.5).
# Use exponential back-off: wait backoff * 2^attempt seconds between retries.

# Solution:
def get_with_retry(url, retries=3, backoff=0.5):
    for attempt in range(retries):
        try:
            r = requests.get(url, timeout=8)
            r.raise_for_status()
            return r.json()
        except requests.exceptions.RequestException as e:
            wait = backoff * (2 ** attempt)
            print(f"Attempt {attempt + 1} failed ({e}). Retrying in {wait:.1f}s…")
            if attempt < retries - 1:
                time.sleep(wait)
    print("All retries exhausted.")
    return None

result = get_with_retry("https://jsonplaceholder.typicode.com/posts/1")
if result:
    print("Got:", result["title"])


# Exercise 3: Make a request to https://httpbin.org/status/429 (Too Many Requests).
# Check the status code and print a user-friendly rate-limit message.

# Solution:
r = requests.get("https://httpbin.org/status/429", timeout=8)
if r.status_code == 429:
    retry_after = r.headers.get("Retry-After", "unknown")
    print(f"Rate limited. Retry after: {retry_after} seconds")
