# Week 08 Assignments — APIs & Web Requests

**Days 50–56 · Topics: HTTP, GET/POST, JSON, Auth, Error Handling, Pagination**

---

## Assignments

### Day 50 — Intro to APIs
- Make a GET request to `https://httpbin.org/get` and print the origin IP
- Fetch `https://jsonplaceholder.typicode.com/users/1` and print name and email
- Write a `check_api_health(url)` function that returns True if status is 2xx

### Day 51 — GET Requests & Query Parameters
- Fetch posts by userId=3 from JSONPlaceholder and print titles
- Set a custom User-Agent and verify the server saw it via httpbin
- Handle a 2-second timeout on `https://httpbin.org/delay/5` gracefully

### Day 52 — JSON Parsing
- Fetch all 10 JSONPlaceholder users and output a Markdown table: Name | Email | City
- Save the result to `users.json` with pretty indentation
- Count how many users are in each city

### Day 53 — POST Requests & Auth
- POST a new post to JSONPlaceholder and confirm a 201 response
- PUT an update to post ID 1 and print the changed title
- Demonstrate loading an API key from `.env` and using it as a header

### Day 54 — Error Handling
- Write `safe_request(url, retries=3)` with exponential back-off
- Handle 404, 500, timeout, and connection errors separately
- Test against `httpbin.org/status/404`, `/status/500`, and a bad domain

### Day 55 — Pagination
- Fetch all 100 JSONPlaceholder posts using page-by-page requests
- Use a `requests.Session` for the paginated requests
- Print the total count and the title of the last post retrieved

### Day 56 — Project: Weather Dashboard
- Extend the Weather Dashboard to accept `--days 5` and show a 5-day forecast
- Add emoji icons based on WMO weather code (☀️ 🌧️ ❄️ etc.)
- Cache the last result in `weather_cache.json`; skip API call if cache is < 10 min old

---

## Grading Criteria

| Criteria | Points |
|----------|--------|
| Correct use of requests | 30 |
| Error handling present | 30 |
| JSON parsing correct | 20 |
| API key handled securely (env var) | 20 |
| **Total** | **100** |
