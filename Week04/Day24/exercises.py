# Day 24 – Reading Files

import os

# Setup: create a sample file to read in all exercises
SAMPLE_FILE = "sample_day24.txt"
with open(SAMPLE_FILE, "w") as f:
    f.write("Line 1: Python is fun\n")
    f.write("Line 2: Files are powerful\n")
    f.write("Line 3: Reading data is essential\n")
    f.write("Line 4: Always use context managers\n")
    f.write("Line 5: Close your files!\n")


# Exercise 1: Read the entire file content with f.read() and print it.

# Solution:
with open(SAMPLE_FILE, "r") as f:
    content = f.read()
print("=== Full Content ===")
print(content)


# Exercise 2: Read lines into a list with f.readlines() and print each with its number.

# Solution:
with open(SAMPLE_FILE, "r") as f:
    lines = f.readlines()

print("=== Numbered Lines ===")
for i, line in enumerate(lines, start=1):
    print(f"{i}: {line.strip()}")


# Exercise 3: Count the number of words in the file.

# Solution:
with open(SAMPLE_FILE, "r") as f:
    word_count = sum(len(line.split()) for line in f)
print(f"Word count: {word_count}")


# Exercise 4: Search for a keyword and print lines that contain it.

# Solution:
keyword = "file"
print(f"\nLines containing '{keyword}':")
with open(SAMPLE_FILE, "r") as f:
    for line in f:
        if keyword.lower() in line.lower():
            print(" ", line.strip())


# Exercise 5: Handle FileNotFoundError gracefully.

# Solution:
try:
    with open("nonexistent.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("Error: The file does not exist.")

# Cleanup
os.remove(SAMPLE_FILE)
