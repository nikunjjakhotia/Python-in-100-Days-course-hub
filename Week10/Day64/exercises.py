# Day 64 – Intro to Flask
# Run with: python exercises.py  (opens http://127.0.0.1:5000)

from flask import Flask

app = Flask(__name__)


# Exercise 1: Add a route for "/" that returns "Hello, Flask!".

@app.route("/")
def index():
    return "Hello, Flask!"


# Exercise 2: Add a route "/about" that returns "About Page".

@app.route("/about")
def about():
    return "About Page"


# Exercise 3: Add a route "/hello/<name>" that returns "Hello, <name>!".

@app.route("/hello/<name>")
def hello(name):
    return f"Hello, {name}!"


# Exercise 4: Add a route "/status" that returns a 200 response with the body "OK".

@app.route("/status")
def status():
    return "OK", 200


# Exercise 5: Add a route "/error" that returns a 404 response with "Not Found".

@app.route("/error")
def error():
    return "Not Found", 404


if __name__ == "__main__":
    print("Routes defined:")
    for rule in app.url_map.iter_rules():
        print(f"  {rule.methods} {rule.rule}")
    app.run(debug=True)
