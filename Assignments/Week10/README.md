<!-- assignments-nav -->
[🏠 Home](../../) | [📚 Week 10 Lessons — Flask Web Development](../../Week10/)

---
<!-- assignments-nav -->

# Week 10 Assignments — Flask Web Development

**Days 64–70 · Topics: Routes, URL Params, Jinja2 Templates, Forms, SQLite + Flask, REST API**

---

## Assignments

### Day 64 — Intro to Flask
- Add 5 routes: `/`, `/about`, `/hello/<name>`, `/status`, and a 404 custom handler
- Print all registered URL rules using `app.url_map`
- Return a different status code for a `/teapot` route (418)

### Day 65 — Routes & URL Parameters
- Build a `/calculator/<float:a>/<op>/<float:b>` route supporting +, -, *, /
- Build a `/palindrome/<string:word>` route that returns `{"is_palindrome": true/false}`
- Use `url_for` to build URLs programmatically and print them

### Day 66 — Jinja2 Templates
- Create a `products.html` template that renders a product table from a list of dicts
- Use template inheritance: create `base.html` with a nav bar and extend it
- Add a Jinja2 filter to format prices as `$9.99`

### Day 67 — Forms & POST
- Build a contact form with name, email, message fields and validation
- Implement the PRG pattern: redirect to `/thank-you` after successful submit
- Add flash messages for success and error states

### Day 68 — SQLite with Flask
- Build a notes app: list, create, and delete notes backed by SQLite
- Use `g` and `teardown_appcontext` for connection management
- Add a `flask init-db` CLI command

### Day 69 — REST API
- Build a full REST API for a `books` resource: GET (list + detail), POST, PUT, DELETE
- Return proper status codes: 201 for create, 204 for delete, 404 for not found
- Register JSON error handlers for 400 and 404

### Day 70 — Project: Task Manager
- Add CSS styling (inline or external)
- Add a task edit feature (change the title)
- Ensure no task is lost on server restart (SQLite persistence)

---

## Grading Criteria

| Criteria | Points |
|----------|--------|
| Routes work correctly | 30 |
| Templates render without errors | 20 |
| Forms validated server-side | 20 |
| Database integration correct | 20 |
| Status codes correct | 10 |
| **Total** | **100** |
