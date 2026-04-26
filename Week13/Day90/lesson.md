# Day 90 – Documentation & README

## Learning Objectives
- Write a professional README that tells the full story of your project
- Add docstrings to public functions
- Create a `requirements.txt` and run instructions

---

## What Makes a Great README?

```markdown
# Project Name

One-sentence description.

## Features
- Feature 1
- Feature 2

## Quick Start
\`\`\`bash
git clone https://github.com/you/project
cd project
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
python app.py
\`\`\`

## Usage
(Screenshots or GIFs of the app in action)

## Project Structure
\`\`\`
project/
├── app.py
├── db.py
└── ...
\`\`\`

## Technologies Used
- Python 3.12
- SQLite
- Flask (optional)

## Author
[Your Name](https://github.com/you)
```

---

## Docstrings

```python
def add_expense(date: str, description: str, amount: float, category_id: int) -> int:
    """Insert a new expense row and return its auto-generated id.

    Args:
        date: ISO 8601 date string, e.g. '2026-01-15'
        description: Short label for the expense
        amount: Positive dollar amount
        category_id: FK referencing categories.id

    Returns:
        The new expense's integer id.
    """
```

---

## `requirements.txt`

```bash
pip freeze > requirements.txt
```

Pin your versions — future installers will get the exact same environment.

---

## `.gitignore`

```
venv/
__pycache__/
*.pyc
*.db
.env
```

---

## Key Takeaways
- The README is the first thing a hiring manager or collaborator sees — make it count
- Docstrings on public functions let IDEs and tools like `help()` show documentation
- Always include Quick Start instructions — assume the reader has a fresh machine

---

## Exercises
See `exercises.py`
