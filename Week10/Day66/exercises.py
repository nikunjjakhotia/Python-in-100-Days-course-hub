# Day 66 – Templates with Jinja2
# NOTE: This file shows the Python side. Template files would live in templates/.
# The Jinja2 environment is used standalone here to demonstrate template rendering
# without needing a running Flask server.

from jinja2 import Environment, BaseLoader

env = Environment(loader=BaseLoader())


# Exercise 1: Render a simple greeting template with a variable.

tmpl = env.from_string("Hello, {{ name }}! You have {{ count }} new messages.")
print(tmpl.render(name="Alice", count=3))


# Exercise 2: Render a template with a for loop over a list of products.

products = [
    {"name": "Widget",   "price": 9.99},
    {"name": "Gadget",   "price": 24.99},
    {"name": "Sprocket", "price": 4.49},
]

tmpl2 = env.from_string("""
Products:
{% for p in products %}
  - {{ p.name }}: ${{ p.price }}
{% endfor %}
""")
print(tmpl2.render(products=products))


# Exercise 3: Render a conditional — show "Admin" badge if role == "admin".

tmpl3 = env.from_string("""
User: {{ user }}
{% if role == "admin" %}[ADMIN]{% else %}[Member]{% endif %}
""")
print(tmpl3.render(user="Bob", role="admin"))
print(tmpl3.render(user="Carol", role="member"))


# Exercise 4: Use a Jinja2 filter to uppercase a name and round a price.

tmpl4 = env.from_string("{{ name | upper }} — ${{ price | round(2) }}")
print(tmpl4.render(name="python course", price=19.999))


# Exercise 5 (Flask): In a real Flask app, what does render_template return?
# Answer: It returns a complete HTML string (the rendered template) wrapped
# in a Flask Response object with Content-Type: text/html.
print("\nrender_template returns a Flask Response with the rendered HTML string.")
