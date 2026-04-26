# Day 26 – os & pathlib
import os
from pathlib import Path

# Exercise 1: Print the current working directory and list files in it.

# Solution:
print("CWD:", os.getcwd())
print("\nFiles in current directory:")
for name in os.listdir("."):
    print(" ", name)


# Exercise 2: Create a nested directory structure using pathlib.

# Solution:
test_dir = Path("test_workspace/logs/2025")
test_dir.mkdir(parents=True, exist_ok=True)
print(f"\nCreated: {test_dir}")
print("Exists:", test_dir.exists())


# Exercise 3: Create 3 text files inside the new directory and list them.

# Solution:
for i in range(1, 4):
    file = test_dir / f"log_{i:02d}.txt"
    file.write_text(f"Log entry {i}\n")

print("\nFiles created:")
for f in sorted(test_dir.iterdir()):
    print(f" {f.name} — {f.stat().st_size} bytes")


# Exercise 4: Rename the first log file.

# Solution:
old = test_dir / "log_01.txt"
new = test_dir / "log_renamed.txt"
old.rename(new)
print(f"\nRenamed to: {new.name}")


# Exercise 5: Clean up — delete all files and the directory tree.

# Solution:
import shutil
shutil.rmtree("test_workspace")
print("\nCleanup complete. test_workspace deleted.")
