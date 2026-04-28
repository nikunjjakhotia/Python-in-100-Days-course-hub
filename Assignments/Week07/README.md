<!-- assignments-nav -->
[🏠 Home](../../) | [📚 Week 07 Lessons — Modules & Packages](../../Week07/)

---
<!-- assignments-nav -->

# Week 07 Assignments — Modules & Packages

**Days 43–49 · Topics: Import, Standard Library, Custom Modules, Packages, venv, pip**

---

## Assignments

### Day 43 — Intro to Modules
- Import `math` and `random`; write a function that generates a random point inside a unit circle
- Import `datetime`; write a function that returns how many days until your next birthday
- Write a module-style file with a `__name__ == "__main__"` guard

### Day 44 — Standard Library
- Use `os` to list all `.py` files in the current directory (non-recursive)
- Use `sys.argv` to build a CLI tool that greets a name passed as an argument
- Use `random.choices` with weights to simulate a biased coin flip 1000 times

### Day 45 — Creating Your Own Modules
- Create a `text_utils.py` module with: `word_count`, `sentence_count`, `most_common_word`
- Import it in a main script and process a paragraph of text
- Add the `__name__` guard with a demo

### Day 46 — Packages & `__init__.py`
- Create a `validators` package with `email.py`, `phone.py`, and `url.py` modules
- Re-export all validators from `__init__.py` so callers write `from validators import validate_email`
- Write a demo script that validates a list of contact records

### Day 47 — Virtual Environments & pip
- Create a venv, install `rich` and `python-dotenv`, and freeze to `requirements.txt`
- Write a script that reads a `.env` file and prints each variable (masking values with `****`)
- Describe in a comment what goes in `.gitignore` and why

### Day 48 — Third-Party Libraries
- Use `rich` to print a coloured table of your top 5 Python projects
- Use `python-dotenv` to load an API key and print whether it's set
- Research and write a 3-sentence summary of one library you'd use in your career

### Day 49 — Project: Utility Library
- Extend `pyutils` with a `colors` module: `hex_to_rgb(hex)`, `rgb_to_hex(r,g,b)`
- Add `__version__ = "1.0.0"` to `__init__.py`
- Write a `README.md` for the package describing each module

---

## Grading Criteria

| Criteria | Points |
|----------|--------|
| Correct import usage | 30 |
| Package structure correct | 30 |
| venv + requirements.txt present | 20 |
| Code quality & docs | 20 |
| **Total** | **100** |
