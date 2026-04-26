# Day 67 – Forms & POST Requests
# Uses Flask test client so no browser needed.

from flask import Flask, request, redirect, url_for, jsonify

app = Flask(__name__)
app.secret_key = "test-secret"

submissions = []   # in-memory store for demo


@app.route("/contact", methods=["GET"])
def contact_form():
    return """
    <form method="POST" action="/contact">
      <input name="name"    placeholder="Name"    required>
      <input name="email"   placeholder="Email"   required type="email">
      <input name="message" placeholder="Message">
      <button type="submit">Send</button>
    </form>
    """


@app.route("/contact", methods=["POST"])
def submit_contact():
    name    = request.form.get("name",    "").strip()
    email   = request.form.get("email",   "").strip()
    message = request.form.get("message", "").strip()

    errors = []
    if not name:
        errors.append("Name is required.")
    if not email or "@" not in email:
        errors.append("Valid email is required.")
    if errors:
        return jsonify({"errors": errors}), 400

    submissions.append({"name": name, "email": email, "message": message})
    return redirect(url_for("thank_you"))


@app.route("/thank-you")
def thank_you():
    return "Thank you! Your message was received."


@app.route("/submissions")
def list_submissions():
    return jsonify(submissions)


# ─── Test with Flask test client ──────────────────────────────────────────────

if __name__ == "__main__":
    client = app.test_client()

    # Exercise 1: GET /contact — should return 200.
    r = client.get("/contact")
    print("GET /contact:", r.status_code)

    # Exercise 2: POST valid data — should redirect to /thank-you.
    r = client.post("/contact", data={"name": "Alice", "email": "a@example.com", "message": "Hi"})
    print("POST valid:", r.status_code, r.headers.get("Location"))

    # Exercise 3: POST missing name — should return 400.
    r = client.post("/contact", data={"email": "b@example.com"})
    print("POST missing name:", r.status_code, r.get_json())

    # Exercise 4: Check submissions list.
    r = client.get("/submissions")
    print("Submissions:", r.get_json())

    app.run(debug=True)
