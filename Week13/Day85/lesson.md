# Day 85 – Capstone Planning & Architecture

## Learning Objectives
- Choose a capstone project scope that showcases your full skill set
- Write a one-page technical spec before writing any code
- Design a layered architecture: data, logic, and UI

---

## Capstone Project Ideas

Pick one that genuinely interests you:

| Project | Key Skills |
|---------|-----------|
| Personal Finance Tracker | SQLite, pandas, matplotlib |
| Job Application Tracker | Flask, SQLite, HTML forms |
| Weather Forecast CLI | APIs, JSON, rich |
| News Aggregator | Web scraping, SQLite, Flask |
| Habit Tracker | SQLite, CLI, schedule |

---

## Writing a Technical Spec

A good spec answers five questions:

1. **What problem does it solve?**  
   "I want to track my monthly expenses and see where my money goes."

2. **Who uses it?** (scope: single user CLI, multi-user web app, etc.)

3. **What are the core features?** (3–5 bullets, not a wish list)

4. **What data does it store?** (sketch the tables/fields)

5. **What technologies will you use?**

---

## Architecture Layers

```
┌─────────────────────────────────┐
│  Presentation (CLI / Flask UI)  │  ← talk to the user
├─────────────────────────────────┤
│  Business Logic (core functions) │  ← pure Python, no I/O
├─────────────────────────────────┤
│  Data Layer (SQLite / CSV)       │  ← read/write persistence
└─────────────────────────────────┘
```

Keep the layers separate — your business logic should not import Flask, and your routes should not write SQL directly.

---

## Milestone Plan

| Day | Milestone |
|-----|-----------|
| 85 | Spec written, architecture decided |
| 86 | Scaffold + schema + seed data |
| 87 | Core feature 1 working end-to-end |
| 88 | Core feature 2 working end-to-end |
| 89 | Tests written |
| 90 | Docs + README |
| 91 | Final polish, edge cases |

---

## Key Takeaways
- Write the spec first — it saves hours of rework later
- Start with the smallest version that proves the core idea works
- Separate concerns: data, logic, UI in distinct modules

---

## Exercises
See `exercises.py`
