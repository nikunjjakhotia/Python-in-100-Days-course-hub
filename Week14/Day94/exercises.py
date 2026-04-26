# Day 94 – Building Portfolio Projects

# Exercise 1: Score your capstone project against the depth checklist.

CHECKLIST = [
    ("Solves a real problem",                  True),
    ("Input validation with error messages",   True),
    ("Unit tests for core logic",              True),   # change to False if not done yet
    ("README with Quick Start + screenshot",   False),  # update once README is written
    ("Clean git history (conventional commits)", True),
    ("No hardcoded secrets",                   True),
]

print("Portfolio Project Depth Checklist")
print("=" * 45)
for item, done in CHECKLIST:
    status = "✓" if done else "✗  ← TODO"
    print(f"  [{status}] {item}")

score = sum(1 for _, done in CHECKLIST if done)
print(f"\nScore: {score}/{len(CHECKLIST)}")
if score == len(CHECKLIST):
    print("Ready to showcase!")
else:
    missing = [item for item, done in CHECKLIST if not done]
    print("Still needed:", missing)


# Exercise 2: Write a project case study paragraph.

def project_case_study(name, problem, solution, tech, challenge, result, url):
    return f"""
PROJECT: {name}
{'─' * 40}
Problem   : {problem}
Solution  : {solution}
Tech Stack: {', '.join(tech)}
Challenge : {challenge}
Result    : {result}
Code      : {url}
"""

study = project_case_study(
    name      = "Expense Tracker",
    problem   = "No easy way to track where monthly money goes",
    solution  = "Built a CLI app with SQLite that categorises expenses and produces monthly reports",
    tech      = ["Python", "SQLite", "unittest"],
    challenge = "Designing a clean separation between validation logic and database code",
    result    = "Personal tool I use every day; processes hundreds of rows instantly",
    url       = "https://github.com/nikunjjakhotia/expense-tracker",
)
print(study)


# Exercise 3: Identify 3 projects from this course to polish into portfolio pieces.

PROJECTS_TO_POLISH = [
    {"day": 49, "name": "pyutils library",    "next_step": "Add type hints, docstrings, publish to PyPI"},
    {"day": 56, "name": "Weather Dashboard",  "next_step": "Add emoji icons + cache last result"},
    {"day": 70, "name": "Flask Task Manager", "next_step": "Add CSS styling + deploy to Render"},
]
print("Projects to polish:")
for p in PROJECTS_TO_POLISH:
    print(f"  Day {p['day']:>3}: {p['name']:<25} → {p['next_step']}")
