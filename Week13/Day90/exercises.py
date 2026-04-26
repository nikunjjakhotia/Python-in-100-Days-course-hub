# Day 90 – Documentation & README

# Exercise 1: Write a well-formed docstring for each of these functions.

def add_expense(date_str: str, description: str, amount: float, category_id: int) -> int:
    """Insert a new expense into the database and return its id.

    Args:
        date_str: ISO 8601 date string, e.g. '2026-01-15'.
        description: Short label for the expense (non-empty).
        amount: Positive dollar value.
        category_id: Foreign key referencing categories.id.

    Returns:
        The auto-generated integer id of the new row.

    Raises:
        ValueError: If description is empty or amount is not positive.
    """
    pass   # implementation would call the DB

def monthly_summary(year: int, month: int) -> list:
    """Return total spending per category for a given year/month.

    Args:
        year: Four-digit year, e.g. 2026.
        month: Month as integer 1–12.

    Returns:
        List of dicts, each with 'category' (str) and 'total' (float),
        sorted by total descending. Empty list if no data.
    """
    pass


# Exercise 2: Print a sample README outline for your capstone project.

README = """
# Expense Tracker

A command-line personal finance tracker backed by SQLite.

## Features
- Add, list, and delete daily expenses
- Categorise spending (Food, Transport, Housing…)
- Monthly summary report by category

## Quick Start
\`\`\`bash
git clone https://github.com/you/expense-tracker
cd expense-tracker
python -m venv venv && source venv/bin/activate  # Windows: venv\\Scripts\\activate
pip install -r requirements.txt
python app.py
\`\`\`

## Project Structure
\`\`\`
expense_tracker/
├── app.py       — CLI entry point
├── db.py        — SQLite helper functions
├── logic.py     — Validation & business rules
├── reports.py   — Monthly/category summaries
└── tests.py     — Unit tests
\`\`\`

## Technologies
- Python 3.12
- SQLite (stdlib sqlite3)

## Author
[Nikunj Jakhotia](https://github.com/nikunjjakhotia)
"""

print(README)


# Exercise 3: Generate a minimal requirements.txt from a list of third-party packages.

PACKAGES = [
    ("rich",          "13.7.1"),
    ("python-dotenv", "1.0.1"),
]

req_lines = [f"{name}=={ver}" for name, ver in PACKAGES]
print("requirements.txt contents:")
print("\n".join(req_lines))


# Exercise 4: Print a .gitignore for a Python project.

GITIGNORE = """venv/
__pycache__/
*.pyc
*.pyo
*.db
.env
*.egg-info/
dist/
"""
print("\n.gitignore:")
print(GITIGNORE)
