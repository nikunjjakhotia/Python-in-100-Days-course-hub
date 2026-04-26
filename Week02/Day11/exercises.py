# Day 11 – For Loops

# Exercise 1: Print numbers 1 to 20 using a for loop with range().

# Solution:
for i in range(1, 21):
    print(i, end=" ")
print()


# Exercise 2: Sum all elements in a list.

# Solution:
numbers = [10, 25, 3, 47, 8, 16]
total = 0
for n in numbers:
    total += n
print(f"Sum: {total}")


# Exercise 3: Print each character of a string on a new line using a for loop.

# Solution:
word = "Python"
for char in word:
    print(char)


# Exercise 4: Use enumerate() to print a numbered grocery list.

# Solution:
groceries = ["Milk", "Eggs", "Bread", "Butter", "Coffee"]
for i, item in enumerate(groceries, start=1):
    print(f"{i}. {item}")


# Exercise 5: Use zip() to pair student names with their scores and print results.

# Solution:
students = ["Alice", "Bob", "Charlie", "Diana"]
scores = [92, 85, 78, 96]
for student, score in zip(students, scores):
    status = "Pass" if score >= 60 else "Fail"
    print(f"{student}: {score} ({status})")
