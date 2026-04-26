# Day 51 – GET Requests & Query Parameters

import requests

BASE = "https://jsonplaceholder.typicode.com"

# Exercise 1: Fetch posts by userId=1 using a query parameter and print each post title.

# Solution:
r = requests.get(f"{BASE}/posts", params={"userId": 1}, timeout=10)
r.raise_for_status()
for post in r.json():
    print(post["title"])


# Exercise 2: Fetch https://httpbin.org/headers with a custom User-Agent header
# and print the User-Agent value that the server saw.

# Solution:
r = requests.get(
    "https://httpbin.org/headers",
    headers={"User-Agent": "PythonDay51/1.0"},
    timeout=10
)
print(r.json()["headers"]["User-Agent"])


# Exercise 3: Demonstrate timeout handling by requesting https://httpbin.org/delay/5
# with a 2-second timeout. Catch the exception and print a friendly message.

# Solution:
try:
    r = requests.get("https://httpbin.org/delay/5", timeout=2)
except requests.exceptions.Timeout:
    print("Request timed out — server took too long.")


# Exercise 4: Download the image at https://httpbin.org/image/png and save it
# as "test_image.png". Print the file size in bytes.

# Solution:
import os

r = requests.get("https://httpbin.org/image/png", timeout=10)
r.raise_for_status()
with open("test_image.png", "wb") as f:
    f.write(r.content)
print(f"Saved test_image.png — {os.path.getsize('test_image.png')} bytes")
