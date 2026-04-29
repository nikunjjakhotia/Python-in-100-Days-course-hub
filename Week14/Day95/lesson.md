<!-- nav -->
[← Day 94](../Day94/lesson.md) | [🏠 Home](../../) | [Day 96 →](../Day96/lesson.md)

---
<!-- nav -->

# Day 95 – Contributing to Open Source

## Learning Objectives
- Find beginner-friendly issues on GitHub
- Follow the contribution workflow (fork → branch → PR)
- Write a good pull request description

---

## Why Contribute?

- Real-world code exposure beyond tutorials
- Visible proof of collaboration skills
- Network with working developers
- Learn professional Git workflows

---

## Finding Issues

Search GitHub with these filters:
```
label:"good first issue" language:Python
label:"help wanted" language:Python is:open
```

Good beginner repos:
- `python/cpython` documentation
- `pallets/flask` (docs, small fixes)
- `pandas-dev/pandas` (docs, tests)
- Any package you actually use

---

## Contribution Workflow

```bash
# 1. Fork the repo on GitHub, then:
git clone https://github.com/YOU/project-name.git
cd project-name

# 2. Create a feature branch
git checkout -b fix/typo-in-readme

# 3. Make your changes
# Edit files...

# 4. Commit using conventional commits
git add README.md
git commit -m "docs: fix typo in installation section"

# 5. Push and open a PR
git push origin fix/typo-in-readme
# → GitHub will show a "Compare & pull request" button
```

---

## Writing a Good PR Description

```markdown
## What this PR does
Fixes a typo in the README installation section ("installaton" → "installation").

## Why
Makes the docs clearer for new users.

## Testing
No code changes — documentation only.
```

---

## PR Etiquette
- One change per PR — don't bundle unrelated fixes
- Respond to reviewer comments within a day or two
- Don't take feedback personally — it's about the code
- Thank reviewers

---

## Key Takeaways
- Start with docs, tests, or small bug fixes — they're merged fastest
- Read `CONTRIBUTING.md` before opening an issue
- Your merged PR is permanently visible on GitHub — it counts as experience

---

## Exercises
See `exercises.py`

---

<!-- nav -->
[📝 Exercises](https://github.com/nikunjjakhotia/Python-in-100-Days-course-hub/blob/main/Week14/Day95/exercises.py) | [← Day 94](../Day94/lesson.md) | [Day 96 →](../Day96/lesson.md)
<!-- nav -->
