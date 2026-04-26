# Day 65 – Routes, URL Parameters & Views

## Learning Objectives
- Use typed URL parameters (`<int:id>`, `<float:value>`)
- Return JSON responses with `jsonify`
- Use `url_for` to build URLs in code

---

## URL Variable Types

```python
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/user/<int:user_id>")
def get_user(user_id):
    return jsonify({"id": user_id, "name": f"User {user_id}"})

@app.route("/item/<string:slug>")
def get_item(slug):
    return jsonify({"slug": slug})

@app.route("/price/<float:value>")
def price(value):
    return jsonify({"price": value, "tax": round(value * 0.20, 2)})
```

Supported types: `string` (default), `int`, `float`, `path`, `uuid`.

---

## `jsonify`

Converts a dict or list to a JSON response with `Content-Type: application/json`:

```python
@app.route("/api/items")
def items():
    return jsonify([{"id": 1, "name": "Widget"}, {"id": 2, "name": "Gadget"}])
```

---

## `url_for`

Build a URL from a view function name instead of hardcoding paths:

```python
from flask import url_for

with app.test_request_context():
    print(url_for("get_user", user_id=42))   # /user/42
    print(url_for("static", filename="style.css"))
```

---

## HTTP Methods

```python
from flask import request

@app.route("/submit", methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        name = request.form.get("name", "")
        return jsonify({"received": name})
    return "Send a POST request with a 'name' field."
```

---

## Key Takeaways
- Type converters (`<int:id>`) validate and convert URL segments automatically
- `jsonify` is the correct way to return JSON — never `json.dumps` directly
- `url_for` keeps your URL references DRY

---

## Exercises
See `exercises.py`
