<!-- nav -->
[← Day 76](../Day76/lesson.md) | [🏠 Home](../../) | [Day 78 →](../../Week12/Day78/lesson.md)

---
<!-- nav -->

# Day 77 – Project: File Organiser Bot

## What You're Building
A script that watches a folder (e.g. `Downloads`) and moves files into sub-folders by extension: `Images/`, `Documents/`, `Videos/`, `Code/`, `Other/`.

---

## Learning Objectives
- Apply `pathlib` and `shutil` to automate file management
- Use a mapping dict to determine destination
- Handle edge cases: duplicates, unknown extensions, same-name files

---

## Extension Map

```python
CATEGORIES = {
    "Images":    {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg"},
    "Documents": {".pdf", ".docx", ".doc", ".xlsx", ".pptx", ".txt", ".md"},
    "Videos":    {".mp4", ".mkv", ".avi", ".mov", ".wmv"},
    "Audio":     {".mp3", ".wav", ".flac", ".aac"},
    "Code":      {".py", ".js", ".ts", ".html", ".css", ".json", ".yaml"},
    "Archives":  {".zip", ".tar", ".gz", ".rar", ".7z"},
}
```

---

## Core Algorithm

```python
from pathlib import Path
import shutil

def categorise(extension: str) -> str:
    for category, exts in CATEGORIES.items():
        if extension.lower() in exts:
            return category
    return "Other"

def organise(folder: Path, dry_run: bool = False) -> None:
    for f in folder.iterdir():
        if f.is_file():
            dest_dir  = folder / categorise(f.suffix)
            dest_file = dest_dir / f.name
            # resolve name collision
            counter = 1
            while dest_file.exists():
                dest_file = dest_dir / f"{f.stem}_{counter}{f.suffix}"
                counter += 1
            if dry_run:
                print(f"Would move: {f.name} → {dest_dir.name}/")
            else:
                dest_dir.mkdir(exist_ok=True)
                shutil.move(str(f), dest_file)
                print(f"Moved: {f.name} → {dest_dir.name}/")
```

---

## Dry Run

Always implement a `--dry-run` mode that prints what would happen without moving anything. It lets users preview before committing.

---

## Stretch Goals
- Accept the target folder as a command-line argument (`sys.argv`)
- Add a log file that records every move with a timestamp
- Add `--undo` support using a JSON log of moves

---

## Exercises
See `exercises.py`

---

<!-- nav -->
[📝 Exercises](exercises.py) | [← Day 76](../Day76/lesson.md) | [Day 78 →](../../Week12/Day78/lesson.md)
<!-- nav -->
