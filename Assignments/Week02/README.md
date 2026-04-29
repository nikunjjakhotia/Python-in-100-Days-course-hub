<!-- assignments-nav -->
[🏠 Home](../../) | [📚 Week 02 Lessons — Control Flow](../../Week02/)

---
<!-- assignments-nav -->

# Week 2 Assignment — Quiz Game

**Days 8–14 · Topics: if/elif/else, Comparison Operators, while, for, break/continue, List Comprehensions**

Build an interactive multiple-choice quiz game that tracks the player's score and gives a grade at the end.

---

## 🎯 What You'll Build

A CLI quiz game with at least 10 questions, multiple-choice answers, a live score tracker, and a final results summary.

---

## 📋 Requirements

1. Store at least **10 questions** in a list of dictionaries, each with `"question"`, `"options"` (list of 4), and `"answer"` keys.
2. Use a `for` loop to iterate through questions and display them one at a time with numbered options.
3. Accept the player's answer and use `if/elif/else` to check if it is correct — increment the score on a correct answer.
4. Use a `while` loop to re-prompt the player if they enter an option that isn't 1–4 (input validation).
5. Track and display whether each answer was **correct or wrong** immediately after submission.
6. After all questions, display the **final score**, a percentage, and a letter grade (A ≥ 90 %, B ≥ 70 %, C ≥ 50 %, F < 50 %).
7. Use a list comprehension to build a list of all **incorrectly answered questions** for the review section.
8. Display the review section at the end showing each missed question and the correct answer.

---

## 💡 Hints

- Store questions as: `{"question": "...", "options": ["A", "B", "C", "D"], "answer": "A"}`.
- `enumerate(questions, start=1)` gives the question number automatically.
- `input().strip().upper()` normalises the player's answer before comparing.
- Integer division for percentage: `score / total * 100`.

---

## 📤 How to Submit

1. Save your solution as `Week02_assignment.py` inside this folder.
2. Run a full game end-to-end and confirm there are no errors.
3. Share a screenshot of the final score screen on LinkedIn with **#Python100Days** and tag [@nikunjjakhotia](https://www.linkedin.com/in/nikunjjakhotia/).

---

## ✅ Marking Criteria

| Criterion | Marks |
|-----------|-------|
| 10+ questions stored correctly as a list of dicts | /10 |
| Questions displayed with numbered options and answer accepted | /10 |
| Score tracked and feedback shown after each question | /10 |
| Invalid input re-prompted without crashing | /5 |
| Final score, percentage, and letter grade displayed | /10 |
| Missed questions reviewed at the end via list comprehension | /5 |
| **Total** | **/50** |

---

*If this course is helping you, please ⭐ [star the repo](https://github.com/nikunjjakhotia/Python-in-100-Days-course-hub) — it helps others find it!*
