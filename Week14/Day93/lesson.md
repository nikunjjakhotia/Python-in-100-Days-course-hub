<!-- nav -->
[← Day 92](../Day92/lesson.md) | [🏠 Home](../../) | [Day 94 →](../Day94/lesson.md)

---
<!-- nav -->

# Day 93 – Optimising Your GitHub Profile

## Learning Objectives
- Write a compelling GitHub profile README
- Organise repositories for maximum impact
- Pin the right projects and write good READMEs

---

## GitHub Profile README

Create a repo named exactly `<your-username>/<your-username>` and add a `README.md`. It appears on your profile page.

```markdown
# Hi, I'm [Name] 👋

Python developer passionate about automation, data analysis, and clean code.

## 🛠 Tech Stack
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?logo=flask&logoColor=white)

## 🚀 Featured Projects
| Project | Description | Tech |
|---------|-------------|------|
| [Expense Tracker](link) | CLI app to track personal finances | Python, SQLite |
| [Weather Dashboard](link) | Live weather CLI using free APIs | Python, requests |
| [File Organiser](link) | Automation bot that sorts downloads | Python, pathlib |

## 📈 Stats
![GitHub Stats](https://github-readme-stats.vercel.app/api?username=<you>&show_icons=true)
```

---

## Repository Best Practices

Every pinned repo should have:
1. **Descriptive name** — `expense-tracker` not `project1`
2. **README.md** with Quick Start, Features, and a screenshot/GIF
3. **topics/tags** set (e.g. `python`, `sqlite`, `cli`)
4. **requirements.txt** or `pyproject.toml`
5. **.gitignore** (no `venv/`, `*.db`, `.env` committed)

---

## Commit Hygiene

```
# Bad
git commit -m "fix"
git commit -m "stuff"

# Good
git commit -m "feat: add monthly summary report by category"
git commit -m "fix: validate negative amounts before DB insert"
git commit -m "docs: update README with installation steps"
```

Conventional Commits format: `type: short imperative description`  
Types: `feat`, `fix`, `docs`, `test`, `refactor`, `chore`

---

## Key Takeaways
- Your GitHub profile is your portfolio — treat each repo as a professional product
- Green contribution graph matters less than the quality of what's there
- Good commit messages show professionalism to every hiring manager who browses your repos

---

## Exercises
See `exercises.py`

---

<!-- nav -->
[📝 Exercises](exercises.py) | [← Day 92](../Day92/lesson.md) | [Day 94 →](../Day94/lesson.md)
<!-- nav -->
