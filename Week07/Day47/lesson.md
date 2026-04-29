<!-- nav -->
[← Day 46](../Day46/lesson.md) | [🏠 Home](../../) | [Day 48 →](../Day48/lesson.md)

---
<!-- nav -->

# Day 47 – Virtual Environments & pip

## Learning Objectives
- Create and activate a virtual environment
- Install, upgrade, and remove packages with pip
- Freeze and recreate dependencies with `requirements.txt`

---

## Why Virtual Environments?

Each project can depend on different package versions. A virtual environment gives each project its own isolated Python installation so versions never conflict.

---

## Creating & Activating

```bash
# Create
python -m venv venv

# Activate
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# You'll see (venv) in your prompt.

# Deactivate when done
deactivate
```

---

## pip Basics

```bash
pip install requests             # install latest
pip install requests==2.28.0     # install specific version
pip install --upgrade requests   # upgrade
pip uninstall requests           # remove
pip list                         # show installed packages
pip show requests                # details about one package
```

---

## `requirements.txt`

```bash
pip freeze > requirements.txt    # save current environment
pip install -r requirements.txt  # recreate it elsewhere
```

A typical `requirements.txt`:
```
requests==2.31.0
flask==3.0.2
pandas==2.2.0
```

---

## `.gitignore` the `venv` Folder

Never commit `venv/` to git — it's large and machine-specific. Add it to `.gitignore`:
```
venv/
__pycache__/
*.pyc
```

---

## Key Takeaways
- Always create a `venv` per project — never install packages globally
- `pip freeze` captures the exact environment; `pip install -r` restores it
- Commit `requirements.txt`, never the `venv/` folder

---

## Exercises
See `exercises.py`

---

<!-- nav -->
[📝 Exercises](https://github.com/nikunjjakhotia/Python-in-100-Days-course-hub/blob/main/Week07/Day47/exercises.py) | [🏠 Home](/Python-in-100-Days-course-hub/) | [← Day 46](../Day46/lesson.md) | [Day 48 →](../Day48/lesson.md)
<!-- nav -->
