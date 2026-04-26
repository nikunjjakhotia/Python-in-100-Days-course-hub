# Day 05 – Tuples, Sets & Dictionaries

# Exercise 1: Tuple basics — create, access, and try to modify.

# Solution:
dimensions = (1920, 1080)
print("Width:", dimensions[0])
print("Height:", dimensions[1])
# dimensions[0] = 1280  # Uncommenting this raises: TypeError: 'tuple' object does not support item assignment


# Exercise 2: Set operations — union, intersection, difference.

# Solution:
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("Union:", set1 | set2)
print("Intersection:", set1 & set2)
print("Difference (set1 - set2):", set1 - set2)
set1.add(10)
print("After add:", set1)


# Exercise 3: Dictionary — create, access, add, and use .get() safely.

# Solution:
student = {"name": "Alice", "grade": "A", "age": 16}
print("Name:", student["name"])
print("Age:", student["age"])
student["city"] = "Toronto"
print("Email:", student.get("email", "Not provided"))
print("Updated dict:", student)


# Exercise 4: Loop through dictionary keys and values.

# Solution:
scores = {"Math": 95, "English": 88, "Science": 92}
for subject, score in scores.items():
    print(f"{subject}: {score}")


# Exercise 5: Remove duplicates from a list using a set.

# Solution:
raw = [1, 2, 2, 3, 4, 4, 4, 5]
unique = list(set(raw))
unique.sort()
print("Unique sorted:", unique)
