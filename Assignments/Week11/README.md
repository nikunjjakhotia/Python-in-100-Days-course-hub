<!-- assignments-nav -->
[🏠 Home](../../) | [📚 Week 11 Lessons — Automation](../../Week11/)

---
<!-- assignments-nav -->

# Week 11 Assignment — File Organiser Bot

**Days 71–77 · Topics: pathlib, shutil, BeautifulSoup, CSV Reports, Email Automation, Scheduling**

Build a script that automatically organises a messy folder by file type, logs every move, generates a CSV report, and can run on a schedule.

---

## 🎯 What You'll Build

A hands-free bot: point it at any folder, run it, and files get sorted into subfolders with a full audit trail — ready to schedule as a cron job or Windows Task.

---

## 📋 Requirements

1. Accept the **target folder path** as a command-line argument (`sys.argv[1]` or `argparse`).
2. Use `pathlib.Path` to scan the folder and move files into subfolders by extension: `images/` (.jpg, .png, .gif, .webp), `documents/` (.pdf, .docx, .txt, .md), `code/` (.py, .js, .ts, .html, .css), `archives/` (.zip, .tar, .gz), `other/` (everything else).
3. Add a `--dry-run` flag: when set, print what *would* happen without moving any files.
4. Use `shutil.move()` for the actual moves; create destination subfolders with `Path.mkdir(parents=True, exist_ok=True)`.
5. Append a timestamped entry to `organiser.log` for every file moved (or skipped in dry-run mode) using a context manager in append mode.
6. After each run, write `report.csv` with columns: `filename`, `extension`, `source`, `destination`, `timestamp`, `status` (moved / skipped / error).
7. Handle edge cases: skip files that are already in the correct subfolder, skip hidden files (name starts with `.`), log any `PermissionError` without crashing.
8. Add a `--watch` flag that uses `schedule` to call `organise()` every 60 seconds — press Ctrl+C to stop cleanly.

---

## 💡 Hints

- `Path(folder).glob("*")` yields all items; filter with `p.is_file()`.
- `p.suffix.lower()` gives the normalised extension (e.g. `.PNG` → `.png`).
- `schedule.every(60).seconds.do(organise, folder)` runs your function on a timer.
- Catch `KeyboardInterrupt` around the `while True: schedule.run_pending()` loop for a clean Ctrl+C exit.

---

## 📤 How to Submit

1. Save your solution as `Week11_assignment.py` inside this folder.
2. Create a test folder with 10+ files of mixed types, run in `--dry-run` mode first, then for real.
3. Share a screenshot of `report.csv` on LinkedIn with **#Python100Days** and tag [@nikunjjakhotia](https://www.linkedin.com/in/nikunjjakhotia/).

---

## ✅ Marking Criteria

| Criterion | Marks |
|-----------|-------|
| Files moved into correct subfolders by extension | /15 |
| `--dry-run` flag prints actions without moving files | /10 |
| `organiser.log` appended correctly with timestamps | /10 |
| `report.csv` written with all required columns | /10 |
| Edge cases handled (already sorted, hidden files, errors) | /5 |
| **Total** | **/50** |

---

*If this course is helping you, please ⭐ [star the repo](https://github.com/nikunjjakhotia/Python-in-100-Days-course-hub) — it helps others find it!*
