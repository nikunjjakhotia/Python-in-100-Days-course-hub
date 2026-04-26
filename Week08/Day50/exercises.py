# Day 50 – Intro to APIs

import requests

# Exercise 1: Make a GET request to https://httpbin.org/get and print the status code and URL.

# Solution:
r = requests.get("https://httpbin.org/get", timeout=10)
print(r.status_code)
print(r.json()["url"])


# Exercise 2: Print the response headers as key-value pairs.

# Solution:
for key, value in r.headers.items():
    print(f"{key}: {value}")


# Exercise 3: Fetch a single post from https://jsonplaceholder.typicode.com/posts/1
# and print its title and body.

# Solution:
post = requests.get("https://jsonplaceholder.typicode.com/posts/1", timeout=10)
post.raise_for_status()
data = post.json()
print("Title:", data["title"])
print("Body:", data["body"])


# Exercise 4: Write a function `check_status(url)` that prints whether a URL is
# reachable (2xx), has an error (4xx/5xx), or cannot connect.

# Solution:
def check_status(url):
    try:
        r = requests.get(url, timeout=5)
        if r.ok:
            print(f"{url} → {r.status_code} OK")
        else:
            print(f"{url} → {r.status_code} Error")
    except requests.exceptions.RequestException as e:
        print(f"{url} → Cannot connect: {e}")

check_status("https://httpbin.org/status/200")
check_status("https://httpbin.org/status/404")
