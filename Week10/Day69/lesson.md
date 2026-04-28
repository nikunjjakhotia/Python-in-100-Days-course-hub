<!-- nav -->
[← Day 68](../Day68/lesson.md) | [🏠 Home](../../) | [Day 70 →](../Day70/lesson.md)

---
<!-- nav -->

# Day 69 – Building a REST API with Flask

## Learning Objectives
- Design a RESTful API with proper HTTP methods and status codes
- Use `request.get_json()` for JSON payloads
- Return consistent JSON responses

---

## REST API Design

| Route | Method | Action |
|-------|--------|--------|
| `/api/items` | GET | List all items |
| `/api/items` | POST | Create new item |
| `/api/items/<id>` | GET | Get one item |
| `/api/items/<id>` | PUT | Replace item |
| `/api/items/<id>` | DELETE | Delete item |

---

## In-Memory API Example

```python
from flask import Flask, jsonify, request, abort

app    = Flask(__name__)
items  = {}
next_id = 1

@app.route("/api/items", methods=["GET"])
def list_items():
    return jsonify(list(items.values()))

@app.route("/api/items", methods=["POST"])
def create_item():
    global next_id
    data = request.get_json()
    if not data or "name" not in data:
        abort(400, "Field 'name' is required")
    item = {"id": next_id, "name": data["name"], "price": data.get("price", 0)}
    items[next_id] = item
    next_id += 1
    return jsonify(item), 201

@app.route("/api/items/<int:item_id>", methods=["GET"])
def get_item(item_id):
    item = items.get(item_id)
    if item is None:
        abort(404, f"Item {item_id} not found")
    return jsonify(item)

@app.route("/api/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    item = items.pop(item_id, None)
    if item is None:
        abort(404)
    return "", 204
```

---

## Error Handlers

```python
@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": str(e)}), 404

@app.errorhandler(400)
def bad_request(e):
    return jsonify({"error": str(e)}), 400
```

---

## Key Takeaways
- `request.get_json()` parses a JSON body; returns `None` if the body isn't JSON
- `abort(code)` immediately returns an error response
- Always register error handlers to return JSON errors, not HTML, from an API

---

## Exercises
See `exercises.py`

---

<!-- nav -->
[📝 Exercises](exercises.py) | [← Day 68](../Day68/lesson.md) | [Day 70 →](../Day70/lesson.md)
<!-- nav -->
