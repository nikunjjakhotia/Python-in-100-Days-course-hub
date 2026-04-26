# Day 69 – Building a REST API with Flask

from flask import Flask, jsonify, request, abort

app     = Flask(__name__)
items   = {1: {"id": 1, "name": "Widget", "price": 9.99}}
next_id = 2


@app.errorhandler(404)
def not_found(e):
    return jsonify({"error": str(e)}), 404

@app.errorhandler(400)
def bad_request(e):
    return jsonify({"error": str(e)}), 400


# GET /api/items
@app.route("/api/items")
def list_items():
    return jsonify(list(items.values()))


# GET /api/items/<id>
@app.route("/api/items/<int:item_id>")
def get_item(item_id):
    item = items.get(item_id)
    if item is None:
        abort(404, f"Item {item_id} not found")
    return jsonify(item)


# POST /api/items
@app.route("/api/items", methods=["POST"])
def create_item():
    global next_id
    data = request.get_json()
    if not data or "name" not in data:
        abort(400, "Field 'name' is required")
    item = {"id": next_id, "name": data["name"], "price": data.get("price", 0.0)}
    items[next_id] = item
    next_id += 1
    return jsonify(item), 201


# PUT /api/items/<id>
@app.route("/api/items/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    if item_id not in items:
        abort(404)
    data = request.get_json() or {}
    items[item_id].update({k: v for k, v in data.items() if k in ("name", "price")})
    return jsonify(items[item_id])


# DELETE /api/items/<id>
@app.route("/api/items/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    if items.pop(item_id, None) is None:
        abort(404)
    return "", 204


# ─── Test ─────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    client = app.test_client()

    print("List:", client.get("/api/items").get_json())
    r = client.post("/api/items", json={"name": "Gadget", "price": 24.99})
    print("Created:", r.get_json(), r.status_code)

    print("Get 1:", client.get("/api/items/1").get_json())
    print("Get 99:", client.get("/api/items/99").get_json())

    client.put("/api/items/1", json={"price": 11.99})
    print("Updated 1:", client.get("/api/items/1").get_json())

    client.delete("/api/items/1")
    print("After delete:", client.get("/api/items").get_json())

    app.run(debug=True)
