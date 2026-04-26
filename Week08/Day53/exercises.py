# Day 53 – POST Requests & Authentication

import requests, os

BASE = "https://jsonplaceholder.typicode.com"

# Exercise 1: Create a new post via POST and print the returned id.

# Solution:
payload = {"title": "My First API Post", "body": "Learning APIs with Python!", "userId": 1}
r = requests.post(f"{BASE}/posts", json=payload, timeout=10)
r.raise_for_status()
print("Created post id:", r.json()["id"])


# Exercise 2: Update the post with id=1 using PUT — change the title to "Updated Title".

# Solution:
update = {"id": 1, "title": "Updated Title", "body": "Changed.", "userId": 1}
r = requests.put(f"{BASE}/posts/1", json=update, timeout=10)
r.raise_for_status()
print("Updated title:", r.json()["title"])


# Exercise 3: Delete post id=5 and confirm the response is 200.

# Solution:
r = requests.delete(f"{BASE}/posts/5", timeout=10)
print("Delete status:", r.status_code)  # 200


# Exercise 4: Simulate using an API key loaded from an environment variable.
# Set API_KEY in your shell: export API_KEY=demo123 (or set it in .env).

# Solution:
api_key = os.getenv("API_KEY", "demo_key_not_set")
r = requests.get(
    "https://httpbin.org/headers",
    headers={"X-API-Key": api_key},
    timeout=10
)
print("Key seen by server:", r.json()["headers"].get("X-Api-Key"))


# Exercise 5: Send a POST request with form data (not JSON) to https://httpbin.org/post
# using data= instead of json=, and compare the parsed bodies.

# Solution:
r_json = requests.post("https://httpbin.org/post", json={"mode": "json"}, timeout=10)
r_form = requests.post("https://httpbin.org/post", data={"mode": "form"}, timeout=10)
print("JSON body:", r_json.json()["json"])
print("Form body:", r_form.json()["form"])
