<!-- nav -->
[← Day 65](../Day65/lesson.md) | [🏠 Home](../../) | [Day 67 →](../Day67/lesson.md)

---
<!-- nav -->

# Day 66 – Templates with Jinja2

## Learning Objectives
- Render HTML templates with `render_template`
- Use Jinja2 variables, loops, and conditionals
- Extend a base layout template

---

## Why Templates?

HTML strings in Python code are hard to maintain. Templates keep HTML separate and let you inject Python data safely.

---

## Setup

```
myapp/
├── app.py
└── templates/
    ├── base.html
    └── index.html
```

---

## Rendering a Template

```python
# app.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", title="Home", name="Alice")
```

{% raw %}
```html
<!-- templates/index.html -->
<h1>{{ title }}</h1>
<p>Welcome, {{ name }}!</p>
```
{% endraw %}

---

## Jinja2 Syntax

{% raw %}
```html
<!-- Variable -->
<p>{{ user.name }}</p>

<!-- If / else -->
{% if user.logged_in %}
  <a href="/logout">Logout</a>
{% else %}
  <a href="/login">Login</a>
{% endif %}

<!-- For loop -->
<ul>
{% for item in items %}
  <li>{{ item.name }} — ${{ item.price }}</li>
{% endfor %}
</ul>

<!-- Filter -->
<p>{{ name | upper }}</p>
<p>{{ price | round(2) }}</p>
```
{% endraw %}

---

## Base Layout (Template Inheritance)

{% raw %}
```html
<!-- templates/base.html -->
<!DOCTYPE html>
<html>
<head><title>{% block title %}My App{% endblock %}</title></head>
<body>
  <nav><a href="/">Home</a> | <a href="/about">About</a></nav>
  {% block content %}{% endblock %}
</body>
</html>
```
{% endraw %}

{% raw %}
```html
<!-- templates/index.html -->
{% extends "base.html" %}
{% block title %}Home{% endblock %}
{% block content %}
  <h1>Welcome!</h1>
{% endblock %}
```
{% endraw %}

---

## Key Takeaways
{% raw %}
- Templates live in the `templates/` folder — Flask finds them automatically
- `{{ }}` outputs variables; `{% %}` runs logic
- `{% extends %}` and `{% block %}` enable reusable layouts
{% endraw %}

---

## Exercises
See `exercises.py`

---

<!-- nav -->
[📝 Exercises](https://github.com/nikunjjakhotia/Python-in-100-Days-course-hub/blob/main/Week10/Day66/exercises.py) | [🏠 Home](/Python-in-100-Days-course-hub/) | [← Day 65](../Day65/lesson.md) | [Day 67 →](../Day67/lesson.md)
<!-- nav -->
