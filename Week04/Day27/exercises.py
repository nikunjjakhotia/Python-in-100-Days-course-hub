# Day 27 – File I/O Challenges
import os

# Setup
with open("story.txt", "w") as f:
    f.write("""Python is a versatile language.
Python is used in web development.
Python is great for data science.
Python powers automation and AI.
Many developers love Python.
Python has a friendly community.
""")

with open("events.log", "w") as f:
    f.write("""2025-01-01 INFO Application started
2025-01-01 ERROR Database connection failed
2025-01-01 INFO User logged in
2025-01-02 ERROR File not found: config.json
2025-01-02 WARNING Disk usage at 85%
2025-01-02 INFO Backup completed
2025-01-03 ERROR Null pointer in module auth
""")


# Exercise 1: Word counter — count total words, lines, and unique words in story.txt.

# Solution:
with open("story.txt") as f:
    content = f.read()

lines = content.strip().split("\n")
words = content.lower().split()
print(f"Lines: {len(lines)}, Words: {len(words)}, Unique: {len(set(words))}")


# Exercise 2: Search and replace — replace "Python" with "Python 3" in story.txt.

# Solution:
with open("story.txt") as f:
    text = f.read()

updated = text.replace("Python", "Python 3")
with open("story_updated.txt", "w") as f:
    f.write(updated)
print("Replaced 'Python' with 'Python 3' in story_updated.txt")


# Exercise 3: Filter ERROR lines from events.log into errors.log.

# Solution:
with open("events.log") as f:
    error_lines = [line for line in f if "ERROR" in line]

with open("errors.log", "w") as f:
    f.writelines(error_lines)

print(f"Found {len(error_lines)} error(s). Written to errors.log")
with open("errors.log") as f:
    print(f.read())


# Exercise 4: Count how many times each log level (INFO, WARNING, ERROR) appears.

# Solution:
counts = {"INFO": 0, "WARNING": 0, "ERROR": 0}
with open("events.log") as f:
    for line in f:
        for level in counts:
            if level in line:
                counts[level] += 1

for level, count in counts.items():
    print(f"{level}: {count}")


# Exercise 5: Write a function that appends a new event to events.log.

# Solution:
from datetime import date

def log_event(level, message, filepath="events.log"):
    entry = f"{date.today()} {level} {message}\n"
    with open(filepath, "a") as f:
        f.write(entry)

log_event("INFO", "Day 27 exercises completed successfully")
print("Appended new log entry.")

# Cleanup
for fname in ["story.txt", "story_updated.txt", "events.log", "errors.log"]:
    if os.path.exists(fname):
        os.remove(fname)
