<!-- nav -->
[← Day 66](../Day66/lesson.md) | [🏠 Home](../../) | [Day 68 →](../Day68/lesson.md)

---
<!-- nav -->

# Day 67 – Forms & POST Requests

## Learning Objectives
- Build an HTML form and handle its POST submission in Flask
- Access form data with `request.form`
- Redirect after a successful POST (PRG pattern)

---

## HTML Form

```html
<!-- templates/contact.html -->
<form method="POST" action="/contact">
  <input type="text"  name="name"    placeholder="Your name" required>
  <input type="email" name="email"   placeholder="Email"     required>
  <textarea name="message" placeholder="Message"></textarea>
  <button type="submit">Send</button>
</form>
```

---

## Handling POST in Flask

```python
from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name    = request.form.get("name",    "").strip()
        email   = request.form.get("email",   "").strip()
        message = request.form.get("message", "").strip()

        if not name or not email:
            return render_template("contact.html", error="Name and email are required.")

        # process the data here …
        return redirect(url_for("thank_you"))

    return render_template("contact.html")

@app.route("/thank-you")
def thank_you():
    return "Thank you for your message!"
```

---

## PRG Pattern (Post/Redirect/Get)

Always redirect after a successful POST — this prevents duplicate submissions when the user refreshes the page.

```
POST /contact ──▶ process ──▶ redirect ──▶ GET /thank-you
```

---

## Flash Messages

```python
from flask import flash, session
app.secret_key = "change-this-in-production"

flash("Message sent successfully!", "success")
```

```html
{% for category, msg in get_flashed_messages(with_categories=True) %}
  <div class="alert {{ category }}">{{ msg }}</div>
{% endfor %}
```

---

## Key Takeaways
- `request.form.get("field", "")` safely retrieves form values
- Always validate server-side — client validation can be bypassed
- Use the PRG pattern: redirect after every successful POST

---

## Exercises
See `exercises.py`

---

<!-- nav -->
[📝 Exercises](exercises.py) | [← Day 66](../Day66/lesson.md) | [Day 68 →](../Day68/lesson.md)
<!-- nav -->
