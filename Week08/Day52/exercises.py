# Day 52 – JSON Parsing & Response Handling

import requests, json

BASE = "https://jsonplaceholder.typicode.com"

# Exercise 1: Fetch all users and print a table: Name | Email | City

# Solution:
users = requests.get(f"{BASE}/users", timeout=10).json()
print(f"{'Name':<25} {'Email':<35} {'City'}")
print("-" * 70)
for u in users:
    print(f"{u['name']:<25} {u['email']:<35} {u['address']['city']}")


# Exercise 2: Build a dict mapping userId → list of post titles using /posts.

# Solution:
posts = requests.get(f"{BASE}/posts", timeout=10).json()
by_user = {}
for p in posts:
    uid = p["userId"]
    by_user.setdefault(uid, []).append(p["title"])

for uid, titles in list(by_user.items())[:3]:
    print(f"\nUser {uid} ({len(titles)} posts):")
    for t in titles[:2]:
        print(f"  • {t}")


# Exercise 3: Save the users list to "users.json" with pretty indentation,
# then reload it and print the first user's company name.

# Solution:
with open("users.json", "w") as f:
    json.dump(users, f, indent=2)

with open("users.json") as f:
    loaded = json.load(f)

print("\nFirst user company:", loaded[0].get("company", {}).get("name", "N/A"))


# Exercise 4: Fetch https://jsonplaceholder.typicode.com/todos?completed=false&userId=1
# and count how many incomplete todos user 1 has.

# Solution:
todos = requests.get(
    f"{BASE}/todos",
    params={"completed": "false", "userId": 1},
    timeout=10
).json()
print(f"\nUser 1 incomplete todos: {len(todos)}")
