# Day 35 – Project: Student Report Generator
import os

SUBJECTS = ["Math", "Science", "English"]

students = [
    {"name": "Alice",   "Math": 92, "Science": 88, "English": 95},
    {"name": "Bob",     "Math": 74, "Science": 65, "English": 80},
    {"name": "Charlie", "Math": 55, "Science": 70, "English": 62},
    {"name": "Diana",   "Math": 98, "Science": 96, "English": 99},
    {"name": "Ethan",   "Math": 60, "Science": 58, "English": 65},
]


def get_grade(avg):
    if avg >= 90: return "A"
    if avg >= 80: return "B"
    if avg >= 70: return "C"
    if avg >= 60: return "D"
    return "F"


def generate_report(students, output="student_report.txt"):
    for s in students:
        scores = [s[sub] for sub in SUBJECTS]
        s["avg"] = sum(scores) / len(scores)
        s["grade"] = get_grade(s["avg"])

    ranked = sorted(students, key=lambda s: s["avg"], reverse=True)
    class_avg = sum(s["avg"] for s in students) / len(students)

    header = f"{'Name':<12}" + "".join(f"{sub:>10}" for sub in SUBJECTS) + f"{'Avg':>8}  {'Grade'}"
    sep = "-" * len(header)

    lines = [
        "=" * 50,
        "        STUDENT REPORT CARD",
        "=" * 50,
        header,
        sep,
    ]
    for s in ranked:
        row = f"{s['name']:<12}"
        row += "".join(f"{s[sub]:>10}" for sub in SUBJECTS)
        row += f"{s['avg']:>8.1f}  {s['grade']}"
        lines.append(row)
    lines += [
        sep,
        f"Class average: {class_avg:.1f}",
        "=" * 50,
    ]

    report = "\n".join(lines)
    print(report)

    with open(output, "w") as f:
        f.write(report + "\n")
    print(f"\nReport saved to {output}")


generate_report(students)

# Cleanup
if os.path.exists("student_report.txt"):
    os.remove("student_report.txt")
