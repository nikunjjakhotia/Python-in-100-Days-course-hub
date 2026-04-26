# Day 71 – File System Automation with pathlib & shutil

from pathlib import Path
import shutil, os

# Create a sandbox directory
sandbox = Path("sandbox_day71")
sandbox.mkdir(exist_ok=True)


# Exercise 1: Create three text files inside sandbox and list them.

# Solution:
for i in range(1, 4):
    (sandbox / f"file{i}.txt").write_text(f"Content of file {i}")

print("Files created:")
for f in sandbox.iterdir():
    print(f" ", f.name, f.stat().st_size, "bytes")


# Exercise 2: Rename file1.txt → renamed.txt using Path.rename().

# Solution:
(sandbox / "file1.txt").rename(sandbox / "renamed.txt")
print("\nAfter rename:")
for f in sandbox.iterdir():
    print(" ", f.name)


# Exercise 3: Copy renamed.txt to a sub-folder backup/.

# Solution:
backup = sandbox / "backup"
backup.mkdir(exist_ok=True)
shutil.copy(sandbox / "renamed.txt", backup / "renamed_backup.txt")
print("\nBackup folder:", list(backup.iterdir()))


# Exercise 4: Use glob to find all .txt files in sandbox (non-recursive).

# Solution:
txt_files = list(sandbox.glob("*.txt"))
print("\n.txt files:", [f.name for f in txt_files])


# Exercise 5: Delete the backup folder and all its contents using shutil.rmtree.

# Solution:
shutil.rmtree(backup)
print("\nBackup deleted. sandbox contents:", [f.name for f in sandbox.iterdir()])


# Clean up
shutil.rmtree(sandbox)
print("Sandbox cleaned up.")
