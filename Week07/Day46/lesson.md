# Day 46 – Packages & `__init__.py`

## Learning Objectives
- Understand how a package differs from a module
- Create a package with `__init__.py`
- Use relative and absolute imports inside a package

---

## What Is a Package?

A **package** is a directory that contains an `__init__.py` file (even an empty one).  
It lets you group related modules under a common namespace.

```
mypackage/
├── __init__.py
├── strings.py
└── numbers.py
```

---

## `__init__.py`

This file runs when the package is first imported. Use it to:
- Re-export the most important names so callers don't need deep paths
- Set `__all__` to control `from package import *`

```python
# mypackage/__init__.py
from .strings import capitalize_words
from .numbers import clamp
```

Now callers can write:
```python
from mypackage import capitalize_words, clamp
```

---

## Absolute vs Relative Imports

```python
# absolute — works anywhere
from mypackage.strings import capitalize_words

# relative — only inside the package
from .strings import capitalize_words    # same package
from ..utils import helper               # one level up
```

---

## Nested Packages

```
mypackage/
├── __init__.py
├── io/
│   ├── __init__.py
│   └── reader.py
└── math/
    ├── __init__.py
    └── stats.py
```

```python
from mypackage.io.reader import read_csv
from mypackage.math.stats import mean
```

---

## Key Takeaways
- A package = a folder with `__init__.py`
- Use `__init__.py` to expose a clean public API
- Relative imports (`.module`) keep code portable within the package

---

## Exercises
See `exercises.py`
