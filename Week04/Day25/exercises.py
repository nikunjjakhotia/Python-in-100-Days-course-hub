# Day 25 – Writing Files
import os
from datetime import datetime

# Exercise 1: Write a list of 5 fruits to a file, one per line.

# Solution:
fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]
with open("fruits.txt", "w") as f:
    for fruit in fruits:
        f.write(fruit + "\n")

with open("fruits.txt") as f:
    print("=== fruits.txt ===")
    print(f.read())


# Exercise 2: Append 3 more fruits to the same file.

# Solution:
more_fruits = ["Fig", "Grape", "Honeydew"]
with open("fruits.txt", "a") as f:
    for fruit in more_fruits:
        f.write(fruit + "\n")

with open("fruits.txt") as f:
    all_fruits = f.readlines()
print(f"Total fruits: {len(all_fruits)}")


# Exercise 3: Write a simple CSV file with student names and scores.

# Solution:
students = [("Alice", 95), ("Bob", 88), ("Charlie", 72), ("Diana", 99)]
with open("scores.csv", "w") as f:
    f.write("Name,Score\n")
    for name, score in students:
        f.write(f"{name},{score}\n")

print("\n=== scores.csv ===")
with open("scores.csv") as f:
    print(f.read())


# Exercise 4: Build a simple logger — append timestamped messages to a log file.

# Solution:
def log(message, filepath="app.log"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filepath, "a") as f:
        f.write(f"[{timestamp}] {message}\n")

log("Application started")
log("User logged in: alice")
log("Database connected")

with open("app.log") as f:
    print("=== app.log ===")
    print(f.read())


# Exercise 5: Read scores.csv back and print the student with the highest score.

# Solution:
scores = []
with open("scores.csv") as f:
    next(f)  # skip header
    for line in f:
        name, score = line.strip().split(",")
        scores.append((name, int(score)))

top = max(scores, key=lambda s: s[1])
print(f"Top student: {top[0]} with {top[1]}")

# Cleanup
for fname in ["fruits.txt", "scores.csv", "app.log"]:
    if os.path.exists(fname):
        os.remove(fname)
