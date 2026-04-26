# Day 14 – Project: Quiz Game

questions = [
    {
        "question": "What does print() do?",
        "options": ["A. Saves a file", "B. Outputs text to the screen",
                    "C. Takes user input", "D. Creates a variable"],
        "answer": "B"
    },
    {
        "question": "Which symbol is used for comments in Python?",
        "options": ["A. //", "B. --", "C. #", "D. /* */"],
        "answer": "C"
    },
    {
        "question": "What is the output of: type(3.14)?",
        "options": ["A. <class 'int'>", "B. <class 'number'>",
                    "C. <class 'float'>", "D. <class 'double'>"],
        "answer": "C"
    },
    {
        "question": "Which data structure uses key-value pairs?",
        "options": ["A. List", "B. Tuple", "C. Set", "D. Dictionary"],
        "answer": "D"
    },
    {
        "question": "What does len([1, 2, 3]) return?",
        "options": ["A. 0", "B. 2", "C. 3", "D. 4"],
        "answer": "C"
    },
]

print("=" * 30)
print("    PYTHON QUIZ GAME")
print("=" * 30)

score = 0

for i, q in enumerate(questions, start=1):
    print(f"\nQ{i}: {q['question']}")
    for option in q["options"]:
        print(f"  {option}")

    user_answer = input("Your answer (A/B/C/D): ").strip().upper()

    if user_answer == q["answer"]:
        print("✓ Correct!")
        score += 1
    else:
        print(f"✗ Wrong. The correct answer was: {q['answer']}")

print("\n" + "=" * 30)
print(f"Final Score: {score}/{len(questions)}")

if score == len(questions):
    print("Perfect score! You're a Python pro!")
elif score >= 3:
    print("Great job! You're on your way to Python mastery!")
else:
    print("Keep practicing — you'll get there!")
