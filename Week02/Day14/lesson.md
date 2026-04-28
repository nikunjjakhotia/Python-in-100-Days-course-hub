<!-- nav -->
[← Day 13](../Day13/lesson.md) | [🏠 Home](../../) | [Day 15 →](../../Week03/Day15/lesson.md)

---
<!-- nav -->

# Day 14 – Project: Quiz Game

## What You're Building
A command-line quiz game with multiple-choice questions, score tracking, and a final results summary. This brings together conditionals, loops, lists, and dictionaries.

---

## Learning Objectives
- Use loops to drive a multi-round game
- Use dictionaries to store structured Q&A data
- Track and display a running score

---

## Project Spec

### Features:
1. 5 multiple-choice questions stored as a list of dicts
2. Each question has: `question`, `options` (list), `answer` (correct letter)
3. Player inputs a letter (A/B/C/D) for each question
4. Score is tracked; wrong answers show the correct answer
5. Final screen shows score and a performance message

### Sample Output:
```
=== PYTHON QUIZ GAME ===

Q1: What does print() do?
  A. Saves a file
  B. Outputs text to the screen
  C. Takes user input
  D. Creates a variable

Your answer: B
✓ Correct!

...

Final Score: 4/5
Great job! You're on your way to Python mastery!
```

---

## Skills Used
- Lists of dictionaries
- `for` loops
- `if/elif/else`
- String comparison (`.upper()`)
- f-strings

---

## Starter Code
See `exercises.py` for the full project.

---

## Bonus Challenges
1. Shuffle question order using `random.shuffle()`
2. Add a timer per question using `time` module
3. Let the player choose how many questions to attempt

---

<!-- nav -->
[📝 Exercises](exercises.py) | [← Day 13](../Day13/lesson.md) | [Day 15 →](../../Week03/Day15/lesson.md)
<!-- nav -->
