# Day 85 – Capstone Planning & Architecture

# Exercise 1: Choose your capstone project and write a mini spec below.
# Fill in the sections — this is your planning document.

SPEC = """
PROJECT: (e.g. Expense Tracker / Job Application Tracker / Habit Tracker)

PROBLEM STATEMENT:
  [1–2 sentences: what problem does this solve for the user?]

TARGET USER:
  [Who uses it? Single user CLI? Multi-user web app?]

CORE FEATURES (3–5):
  1.
  2.
  3.

DATA MODEL (tables/fields):
  Table 1: __________  Fields: id, ...
  Table 2: __________  Fields: id, ...

TECHNOLOGIES:
  - Python 3.x
  - SQLite (sqlite3)
  - [Flask? pandas? requests?]

MILESTONE PLAN:
  Day 86: scaffold + schema
  Day 87: feature 1
  Day 88: feature 2 + CLI menu
  Day 89: tests
  Day 90: docs
  Day 91: polish
"""

print("=== My Capstone Spec ===")
print(SPEC)


# Exercise 2: Sketch the directory structure as a string and print it.

# Solution (example — adjust for your project):
STRUCTURE = """
my_capstone/
├── app.py           ← entry point / main menu
├── db.py            ← all SQLite code
├── logic.py         ← business logic & validation
├── reports.py       ← reports / summaries
├── tests.py         ← unittest tests
├── requirements.txt
└── README.md
"""
print("Directory structure:")
print(STRUCTURE)


# Exercise 3: Identify the three architecture layers for your project.

LAYERS = {
    "Presentation":    "CLI menu / Flask routes — talks to the user",
    "Business Logic":  "logic.py — validates data, pure Python functions",
    "Data Layer":      "db.py — reads/writes SQLite",
}
print("Architecture layers:")
for layer, desc in LAYERS.items():
    print(f"  {layer:<20} → {desc}")
