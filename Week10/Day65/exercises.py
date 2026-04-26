# Day 65 – Routes, URL Parameters & Views

from flask import Flask, jsonify, url_for

app = Flask(__name__)

# In-memory "database" for demo purposes
PRODUCTS = {
    1: {"id": 1, "name": "Widget",  "price": 9.99},
    2: {"id": 2, "name": "Gadget",  "price": 24.99},
    3: {"id": 3, "name": "Doohickey", "price": 4.49},
}


# Exercise 1: Route GET /products — return all products as JSON.

@app.route("/products")
def list_products():
    return jsonify(list(PRODUCTS.values()))


# Exercise 2: Route GET /products/<int:pid> — return one product or 404.

@app.route("/products/<int:pid>")
def get_product(pid):
    product = PRODUCTS.get(pid)
    if product is None:
        return jsonify({"error": "Not found"}), 404
    return jsonify(product)


# Exercise 3: Route GET /products/search/<string:keyword> — return products
# whose name contains the keyword (case-insensitive).

@app.route("/products/search/<string:keyword>")
def search_products(keyword):
    results = [p for p in PRODUCTS.values() if keyword.lower() in p["name"].lower()]
    return jsonify(results)


# Exercise 4: Route GET /price/<float:value>/tax — return price + 20% tax.

@app.route("/price/<float:value>/tax")
def calculate_tax(value):
    return jsonify({"price": value, "tax": round(value * 0.20, 2), "total": round(value * 1.20, 2)})


# Exercise 5: Print all registered URL rules and their endpoints using url_for.

if __name__ == "__main__":
    with app.test_request_context():
        for rule in app.url_map.iter_rules():
            if rule.arguments:
                dummy = {arg: 1 for arg in rule.arguments}
                try:
                    built = url_for(rule.endpoint, **dummy)
                    print(f"{rule.endpoint:30} → {built}")
                except Exception:
                    print(f"{rule.endpoint:30} → {rule.rule}")
    app.run(debug=True)
