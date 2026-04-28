<!-- nav -->
[← Day 93](../Day93/lesson.md) | [🏠 Home](../../) | [Day 95 →](../Day95/lesson.md)

---
<!-- nav -->

# Day 94 – Building Portfolio Projects

## Learning Objectives
- Understand what makes a portfolio project stand out
- Turn a simple exercise into a full, showcaseable project
- Write a project case study

---

## What Makes a Portfolio Project Stand Out?

| Ordinary | Showcase-worthy |
|----------|----------------|
| "To-do list" | "To-do list with recurring tasks, SQLite persistence, CSV export, and unittest coverage" |
| "Web scraper" | "News aggregator that scrapes 5 sources, deduplicates by URL, stores in SQLite, and serves a Flask REST API" |
| "Data analysis" | "Sales dashboard that ingests a CSV, cleans nulls, groups by region, and renders a 4-panel Matplotlib report saved as PNG" |

The difference is **depth**: error handling, tests, docs, and a polished demo.

---

## Project Case Study Format (for your portfolio site or LinkedIn)

```
Problem:        What was the pain point?
Solution:       What did you build?
Tech Stack:     Python, Flask, SQLite, pandas
Key Challenges: e.g. "Parsing inconsistent date formats in the CSV"
Result:         "Processes 10k rows in under 2 seconds"
Code:           github.com/you/project
```

---

## Depth Checklist

For each portfolio project, aim to check all of these:

- [ ] Solves a real (even if personal) problem
- [ ] Input validation with helpful error messages
- [ ] Unit tests for core logic
- [ ] README with Quick Start + screenshot
- [ ] Clean git history with conventional commits
- [ ] No hardcoded secrets

---

## Ideas Specific to This Course

- **Week 8 capstone** → polish with rich terminal output + CSV export
- **Week 10 capstone** → add user authentication + deploy on Render/Railway
- **Week 12 capstone** → turn the dashboard into an interactive HTML report with `plotly`

---

## Key Takeaways
- Three polished projects beat twenty half-finished ones on a portfolio
- Write a case study for each project — the story matters as much as the code
- Solve problems you actually have — genuine enthusiasm shows in the code

---

## Exercises
See `exercises.py`

---

<!-- nav -->
[📝 Exercises](exercises.py) | [← Day 93](../Day93/lesson.md) | [Day 95 →](../Day95/lesson.md)
<!-- nav -->
