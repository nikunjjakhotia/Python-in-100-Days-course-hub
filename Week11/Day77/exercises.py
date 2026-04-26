# Day 77 – Project: File Organiser Bot

from pathlib import Path
import shutil

CATEGORIES = {
    "Images":    {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg"},
    "Documents": {".pdf", ".docx", ".doc", ".xlsx", ".pptx", ".txt", ".md"},
    "Videos":    {".mp4", ".mkv", ".avi", ".mov", ".wmv"},
    "Audio":     {".mp3", ".wav", ".flac", ".aac"},
    "Code":      {".py", ".js", ".ts", ".html", ".css", ".json", ".yaml"},
    "Archives":  {".zip", ".tar", ".gz", ".rar", ".7z"},
}


def categorise(extension: str) -> str:
    for category, exts in CATEGORIES.items():
        if extension.lower() in exts:
            return category
    return "Other"


def unique_dest(dest_dir: Path, filename: str) -> Path:
    p = Path(filename)
    dest = dest_dir / filename
    counter = 1
    while dest.exists():
        dest = dest_dir / f"{p.stem}_{counter}{p.suffix}"
        counter += 1
    return dest


def organise(folder: Path, dry_run: bool = False) -> dict:
    moved = {}
    for f in folder.iterdir():
        if not f.is_file():
            continue
        cat      = categorise(f.suffix)
        dest_dir = folder / cat
        dest     = unique_dest(dest_dir, f.name)
        if dry_run:
            print(f"[DRY RUN] {f.name} → {cat}/")
        else:
            dest_dir.mkdir(exist_ok=True)
            shutil.move(str(f), dest)
            print(f"Moved: {f.name} → {cat}/")
        moved.setdefault(cat, []).append(f.name)
    return moved


# ─── Demo ────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # Create a fake downloads folder with sample files
    demo = Path("demo_downloads")
    demo.mkdir(exist_ok=True)

    sample_files = [
        ("photo1.jpg", b"fake jpg"),
        ("report.pdf", b"fake pdf"),
        ("script.py",  b"print('hello')"),
        ("video.mp4",  b"fake video"),
        ("notes.txt",  b"some notes"),
        ("data.json",  b"{}"),
        ("mystery.xyz", b"unknown type"),
    ]
    for name, content in sample_files:
        (demo / name).write_bytes(content)

    print("=== DRY RUN ===")
    organise(demo, dry_run=True)

    print("\n=== ACTUAL RUN ===")
    summary = organise(demo, dry_run=False)

    print("\n=== SUMMARY ===")
    for cat, files in summary.items():
        print(f"  {cat}: {files}")

    # Clean up demo folder
    shutil.rmtree(demo)
    print("\nDemo folder cleaned up.")
