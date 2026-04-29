<!-- assignments-nav -->
[🏠 Home](../../) | [📚 Week 08 Lessons — APIs & Web Requests](../../Week08/)

---
<!-- assignments-nav -->

# Week 8 Assignment — Weather Dashboard CLI

**Days 50–56 · Topics: HTTP, GET/POST, JSON Parsing, Authentication, Error Handling, Pagination**

Build a command-line weather dashboard that fetches live data from a public API, caches results locally, and handles network failures gracefully.

---

## 🎯 What You'll Build

A polished CLI tool a user can run as `python Week08_assignment.py --city London` to get current weather and a 3-day forecast, with local caching so repeat runs are instant.

---

## 📋 Requirements

1. Fetch **current weather** from the [Open-Meteo API](https://open-meteo.com/) (free, no key required) — display temperature, wind speed, and weather condition.
2. Accept a `--city` argument via `sys.argv` or `argparse`; use the Open-Meteo geocoding endpoint to resolve the city name to latitude/longitude before the weather call.
3. Display a **3-day forecast** by requesting the `daily` parameter and formatting each day's high, low, and condition in a table.
4. Implement `safe_get(url, params, retries=3)` with **exponential back-off** (wait 1 s, 2 s, 4 s) — raise a custom `APIError` if all retries fail.
5. Cache the last successful response in `cache.json` — skip the API call if the cached data is **under 10 minutes old** (compare timestamps).
6. Display the **wind speed in both m/s and km/h** — convert in code, not in the API call.
7. Print a clear **error message** (not a traceback) if: the city name is not found, the network is unavailable, or the API returns a non-200 status.
8. Add a `--no-cache` flag that forces a fresh API call even if the cache is still valid.

---

## 💡 Hints

- Open-Meteo geocoding: `https://geocoding-api.open-meteo.com/v1/search?name=<city>&count=1`.
- Cache timestamp: `datetime.datetime.now().isoformat()` → parse back with `datetime.datetime.fromisoformat()`.
- `time.sleep(2 ** attempt)` gives 1 s, 2 s, 4 s back-off.
- `argparse.ArgumentParser()` is cleaner than manual `sys.argv` parsing for multiple flags.

---

## 📤 How to Submit

1. Save your solution as `Week08_assignment.py` inside this folder.
2. Run it with `--city` for two different cities and confirm caching works on the second run.
3. Share a screenshot of the forecast table on LinkedIn with **#Python100Days** and tag [@nikunjjakhotia](https://www.linkedin.com/in/nikunjjakhotia/).

---

## ✅ Marking Criteria

| Criterion | Marks |
|-----------|-------|
| Current weather fetched and displayed with correct fields | /10 |
| City name resolved to coordinates via geocoding endpoint | /10 |
| 3-day forecast displayed in table format | /10 |
| Retry logic with exponential back-off implemented | /10 |
| Caching works — skips API when cache is fresh | /10 |
| **Total** | **/50** |
