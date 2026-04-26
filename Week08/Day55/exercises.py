# Day 55 – Pagination & Rate Limiting

import requests, time

BASE = "https://jsonplaceholder.typicode.com"

# Exercise 1: Fetch all 100 posts using the _page / _limit pagination of JSONPlaceholder.
# Print the total count when done.

# Solution:
def fetch_all_posts():
    all_posts, page = [], 1
    while True:
        r = requests.get(f"{BASE}/posts", params={"_page": page, "_limit": 10}, timeout=10)
        r.raise_for_status()
        data = r.json()
        if not data:
            break
        all_posts.extend(data)
        page += 1
        time.sleep(0.1)   # polite delay
    return all_posts

posts = fetch_all_posts()
print(f"Total posts fetched: {len(posts)}")


# Exercise 2: Rewrite fetch_all_posts() using a requests.Session for connection reuse.

# Solution:
def fetch_all_with_session():
    session = requests.Session()
    all_posts, page = [], 1
    while True:
        r = session.get(f"{BASE}/posts", params={"_page": page, "_limit": 10}, timeout=10)
        r.raise_for_status()
        data = r.json()
        if not data:
            break
        all_posts.extend(data)
        page += 1
    return all_posts

posts2 = fetch_all_with_session()
print(f"Session fetch: {len(posts2)} posts")


# Exercise 3: Print the X-Total-Count header from GET /posts (no pagination).
# This header tells you how many items exist without fetching them all.

# Solution:
r = requests.get(f"{BASE}/posts", timeout=10)
total = r.headers.get("X-Total-Count", "header not present")
print(f"X-Total-Count: {total}")


# Exercise 4: Write a rate-limited fetcher that fetches /posts/1 through /posts/5,
# sleeping 200ms between each request, and prints each post title.

# Solution:
for post_id in range(1, 6):
    r = requests.get(f"{BASE}/posts/{post_id}", timeout=10)
    r.raise_for_status()
    print(f"Post {post_id}: {r.json()['title']}")
    time.sleep(0.2)
