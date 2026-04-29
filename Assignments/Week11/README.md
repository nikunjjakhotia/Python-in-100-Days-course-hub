<!-- assignments-nav -->
[🏠 Home](../../) | [📚 Week 11 Lessons — Automation](../../Week11/)

---
<!-- assignments-nav -->

# Week 11 Assignment: Build a File Organiser Bot

**Days 71–77 · Topics: pathlib, shutil, BeautifulSoup, CSV Reports, Email Automation, Scheduling**

Using the automation skills from Days 71–77, build a script that organises a target folder, logs every action, and runs on a recurring schedule.

## What to Build
- An `organise(folder)` function using `pathlib` that moves files into subfolders by extension (e.g. `images/`, `docs/`, `code/`)
- A `--dry-run` CLI flag that prints what would happen without moving any files
- A timestamped `moves.log` file appended after each run using a context manager
- A CSV summary report (`report.csv`) with columns: file name, source path, destination path, timestamp
- A `schedule` job that calls `organise()` every 60 seconds — press Ctrl+C to stop
