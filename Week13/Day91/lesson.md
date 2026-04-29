<!-- nav -->
[← Day 90](../Day90/lesson.md) | [🏠 Home](../../) | [Day 92 →](../../Week14/Day92/lesson.md)

---
<!-- nav -->

# Day 91 – Final Polish & Code Review

## Learning Objectives
- Perform a self-code-review checklist
- Refactor repeated code into helper functions
- Verify edge cases and add friendly error messages

---

## Self-Review Checklist

Go through your project file by file:

### Correctness
- [ ] Does every feature work on the happy path?
- [ ] What happens if the user enters empty input?
- [ ] What happens if the database is empty?
- [ ] Are numbers validated before arithmetic?

### Code Quality
- [ ] No function longer than ~30 lines
- [ ] No repeated SQL — extract to db functions
- [ ] Variables named clearly (not `x`, `tmp`, `data`)
- [ ] No print-debugging left in the code

### Security
- [ ] All SQL uses `?` placeholders — no string formatting
- [ ] No credentials in source code

### Documentation
- [ ] `README.md` has Quick Start, Features, and Usage sections
- [ ] Key public functions have docstrings

---

## Common Refactors

```python
# Before — repeated formatting
print(f"{e['date']}  {e['description']:<30}  ${e['amount']:.2f}")
print(f"{e['date']}  {e['description']:<30}  ${e['amount']:.2f}")

# After — helper
def format_expense(e):
    return f"{e['date']}  {e['description']:<30}  ${e['amount']:.2f}"
```

---

## Edge Cases to Test

| Scenario | Expected Behaviour |
|----------|--------------------|
| Empty database, list expenses | "No expenses found." |
| Delete ID that doesn't exist | "No expense with that ID." |
| Add expense with amount "abc" | Validation error, no crash |
| Month summary with no data | Empty table, no crash |

---

## Final Commit

```bash
git add .
git commit -m "feat: capstone expense tracker complete"
git push
```

---

## Key Takeaways
- Self-review is a professional skill — build the habit now
- Fix bugs before adding more features — technical debt compounds
- A polished, well-documented project speaks louder on a CV than ten half-finished ones

---

## Exercises
See `exercises.py`

---

<!-- nav -->
[📝 Exercises](https://github.com/nikunjjakhotia/Python-in-100-Days-course-hub/blob/main/Week13/Day91/exercises.py) | [← Day 90](../Day90/lesson.md) | [Day 92 →](../../Week14/Day92/lesson.md)
<!-- nav -->
