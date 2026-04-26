# Day 47 – Virtual Environments & pip
# These exercises are conceptual / scripting tasks — run the shell commands in your terminal.


# Exercise 1: Shell task — create a virtual environment called "venv" and activate it.
# Commands to run in your terminal:
#   python -m venv venv
#   venv\Scripts\activate        (Windows)
#   source venv/bin/activate     (macOS/Linux)
print("Exercise 1: See shell commands above.")


# Exercise 2: Shell task — install the `rich` package and verify with `pip list`.
#   pip install rich
#   pip list
print("Exercise 2: See shell commands above.")


# Exercise 3: Shell task — freeze your environment to requirements.txt.
#   pip freeze > requirements.txt
#   cat requirements.txt   (or type requirements.txt on Windows)
print("Exercise 3: See shell commands above.")


# Exercise 4: Python task — read requirements.txt and print each package name
# (without the version specifier).

import os

req_path = "requirements.txt"
if os.path.exists(req_path):
    with open(req_path) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#"):
                pkg = line.split("==")[0].split(">=")[0].split("<=")[0]
                print(pkg)
else:
    print("requirements.txt not found — run `pip freeze > requirements.txt` first.")


# Exercise 5: Shell task — uninstall `rich` and verify it's gone.
#   pip uninstall rich -y
#   pip list
print("Exercise 5: See shell commands above.")
