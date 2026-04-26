# Day 100 – Course Wrap-Up & What's Next

# Exercise 1: Print your full course completion certificate info.

from datetime import date

CERTIFICATE = {
    "course":     "Python in 100 Days",
    "instructor": "Nikunj Jakhotia",
    "completed":  str(date.today()),
    "topics":     [
        "Python Fundamentals", "Control Flow", "Functions",
        "Error Handling & File I/O", "Data Structures", "OOP",
        "Modules & Packages", "REST APIs", "SQLite & Databases",
        "Flask Web Development", "Automation", "pandas & Data Visualisation",
        "Capstone Project", "Career & Portfolio",
    ],
}

WIDTH = 60
print("=" * WIDTH)
print(f"{'COURSE COMPLETION CERTIFICATE':^{WIDTH}}")
print("=" * WIDTH)
print(f"  Course    : {CERTIFICATE['course']}")
print(f"  Instructor: {CERTIFICATE['instructor']}")
print(f"  Completed : {CERTIFICATE['completed']}")
print(f"\n  Topics covered ({len(CERTIFICATE['topics'])}):")
for topic in CERTIFICATE["topics"]:
    print(f"    ✓ {topic}")
print("=" * WIDTH)
print(f"{'Congratulations!':^{WIDTH}}")
print("=" * WIDTH)


# Exercise 2: Print personalised next-step recommendations.

def recommend_path(interests):
    paths = {
        "web":        ("Web Development", ["Django", "FastAPI", "PostgreSQL"]),
        "data":       ("Data Science",    ["numpy", "scikit-learn", "Jupyter"]),
        "automation": ("Automation/DevOps",["pytest", "Docker", "GitHub Actions"]),
        "building":   ("Keep Building",   ["personal projects", "open source", "freelance"]),
    }
    print("\nRecommended next steps:")
    for interest in interests:
        if interest in paths:
            name, items = paths[interest]
            print(f"\n  Path: {name}")
            for item in items:
                print(f"    → {item}")

recommend_path(["web", "data"])


# Exercise 3: Final self-assessment — rate your confidence in each week's topic.

TOPICS = [
    ("Week 1-2", "Fundamentals & Control Flow"),
    ("Week 3-4", "Functions & Error Handling"),
    ("Week 5-6", "Data Structures & OOP"),
    ("Week 7",   "Modules & Packages"),
    ("Week 8",   "APIs"),
    ("Week 9",   "SQLite"),
    ("Week 10",  "Flask"),
    ("Week 11",  "Automation"),
    ("Week 12",  "pandas & Visualisation"),
    ("Week 13",  "Capstone Project"),
    ("Week 14",  "Career & Portfolio"),
]

# Update ratings honestly: 1=shaky, 2=ok, 3=confident
RATINGS = {topic[0]: 3 for topic in TOPICS}   # placeholder — change your own ratings

print("\n\nSelf-Assessment (1=shaky  2=ok  3=confident):")
print("-" * 50)
for week, topic in TOPICS:
    stars = "★" * RATINGS[week] + "☆" * (3 - RATINGS[week])
    print(f"  {week:<10} {topic:<30} {stars}")

weak = [t for w, t in TOPICS if RATINGS[(w, t)[0]] < 3]
print(f"\nAreas to revisit: {weak if weak else 'All solid! Great work.'}")
print("\nKeep building. Keep learning. 🐍")
