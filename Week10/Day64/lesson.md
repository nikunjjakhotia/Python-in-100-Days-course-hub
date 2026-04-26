# Day 64 – Intro to Flask

## Learning Objectives
- Understand what a web framework does
- Create a Flask app and run it locally
- Know the request/response cycle

---

## What Is Flask?

Flask is a **lightweight web framework** for Python. You define URL routes and the functions that handle them. Flask handles HTTP parsing, routing, and response formatting.

```bash
pip install flask
```

---

## Hello World

```python
# app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)
```

Run it:
```bash
python app.py
# * Running on http://127.0.0.1:5000
```

---

## The Request/Response Cycle

```
Browser                Flask
  │─── GET / ─────────▶│
  │                    │  index() runs
  │◀── 200 "Hello..." ─│
```

---

## `debug=True`

In development, `debug=True`:
- Auto-reloads when you save the file
- Shows a browser error page with traceback

**Never use `debug=True` in production.**

---

## Multiple Routes

```python
@app.route("/")
def home():
    return "Home Page"

@app.route("/about")
def about():
    return "About Page"

@app.route("/hello/<name>")
def hello(name):
    return f"Hello, {name}!"
```

---

## Returning Status Codes

```python
@app.route("/error")
def trigger_error():
    return "Not Found", 404
```

---

## Key Takeaways
- A Flask route pairs a URL pattern with a Python function
- `@app.route()` is the decorator that registers the route
- URL variables are captured with `<name>` syntax

---

## Exercises
See `exercises.py`
