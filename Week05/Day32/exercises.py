# Day 32 – Nested Data Structures

# Exercise 1: Given a list of student dicts, print each student's name and score.

# Solution:
students = [
    {"name": "Alice", "score": 95, "grade": "A"},
    {"name": "Bob",   "score": 82, "grade": "B"},
    {"name": "Charlie", "score": 71, "grade": "C"},
    {"name": "Diana", "score": 99, "grade": "A+"},
]
for s in students:
    print(f"{s['name']:<10} Score: {s['score']}  Grade: {s['grade']}")


# Exercise 2: Find the student with the highest score.

# Solution:
top = max(students, key=lambda s: s["score"])
print(f"\nTop student: {top['name']} ({top['score']})")


# Exercise 3: Group students by grade into a dict of lists.

# Solution:
by_grade = {}
for s in students:
    by_grade.setdefault(s["grade"], []).append(s["name"])
for grade, names in sorted(by_grade.items()):
    print(f"{grade}: {', '.join(names)}")


# Exercise 4: Add a "passed" key (True if score >= 75) to each student dict.

# Solution:
for s in students:
    s["passed"] = s["score"] >= 75
print("\nUpdated records:")
for s in students:
    print(s)


# Exercise 5: Given a nested company dict, print each department's team lead.

# Solution:
company = {
    "engineering": {"lead": "Alice", "team_size": 12},
    "marketing":   {"lead": "Bob",   "team_size": 6},
    "data":        {"lead": "Carol", "team_size": 8},
}
for dept, info in company.items():
    print(f"{dept.capitalize()} lead: {info['lead']} (team of {info['team_size']})")
