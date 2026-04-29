<!-- assignments-nav -->
[🏠 Home](../../) | [📚 Week 08 Lessons — APIs & Web Requests](../../Week08/)

---
<!-- assignments-nav -->

# Week 08 Assignment: Build a Live Data CLI Dashboard

**Days 50–56 · Topics: HTTP, GET/POST, JSON Parsing, Auth, Error Handling, Pagination**

Using the API skills from Days 50–56, build a command-line dashboard that fetches live data from two public APIs, handles failures gracefully, and caches results locally.

## What to Build
- Fetch current weather from the Open-Meteo API (free, no key required) and display temperature, wind speed, and condition
- Fetch data from a second public API of your choice (e.g. REST Countries, PokeAPI, or JSONPlaceholder)
- A `safe_request(url, retries=3)` function with exponential back-off for handling network and timeout errors
- Cache the last successful response in `cache.json`; skip the API call if the cache is under 10 minutes old
- Accept at least one `sys.argv` argument (e.g. `--city` or `--country`) to customise the request
