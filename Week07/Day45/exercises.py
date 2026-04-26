# Day 45 – Creating Your Own Modules
# NOTE: These exercises are self-contained in one file to make them runnable.
# In a real project each function group would live in its own .py file.


# Exercise 1: Write a function `celsius_to_fahrenheit(c)` and a function
# `fahrenheit_to_celsius(f)`. Call both and verify they round-trip correctly.

# Solution:
def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

c = 100
f = celsius_to_fahrenheit(c)
print(f"{c}°C = {f}°F")
print(f"{f}°F = {fahrenheit_to_celsius(f):.1f}°C")


# Exercise 2: Write a `is_palindrome(text)` function.
# Strip punctuation and ignore case. Test with "racecar" and "hello".

# Solution:
import re

def is_palindrome(text):
    cleaned = re.sub(r"[^a-z0-9]", "", text.lower())
    return cleaned == cleaned[::-1]

for word in ["racecar", "hello", "A man a plan a canal Panama"]:
    print(f"'{word}' → {is_palindrome(word)}")


# Exercise 3: Write a module-style `stats` block with:
# mean(nums), median(nums), and mode(nums).
# Use the __name__ guard to run a quick demo.

# Solution:
from statistics import mean, median, mode

def stats_summary(nums):
    return {
        "mean":   mean(nums),
        "median": median(nums),
        "mode":   mode(nums),
    }

if __name__ == "__main__":
    data = [4, 1, 2, 2, 3, 5, 2]
    print(stats_summary(data))


# Exercise 4: Create a simple lookup "database" as a dict in this file,
# then write a `find_by_name(name)` function that searches it.

# Solution:
CONTACTS = {
    "Alice": "alice@example.com",
    "Bob":   "bob@example.com",
    "Carol": "carol@example.com",
}

def find_by_name(name):
    return CONTACTS.get(name, "Not found")

print(find_by_name("Bob"))
print(find_by_name("Dave"))
