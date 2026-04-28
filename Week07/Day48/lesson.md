<!-- nav -->
[← Day 47](../Day47/lesson.md) | [🏠 Home](../../) | [Day 49 →](../Day49/lesson.md)

---
<!-- nav -->

# Day 48 – Popular Third-Party Libraries

## Learning Objectives
- Know the most useful third-party Python libraries by category
- Understand when to reach for each one
- Read a library's documentation and run a quick example

---

## Web & HTTP
| Library | Use |
|---------|-----|
| `requests` | HTTP requests (GET, POST, etc.) |
| `httpx` | Async-friendly alternative to requests |
| `flask` | Lightweight web framework |
| `fastapi` | Modern async REST API framework |

---

## Data & Science
| Library | Use |
|---------|-----|
| `pandas` | Tabular data manipulation |
| `numpy` | Numerical arrays and linear algebra |
| `matplotlib` | 2-D plotting |
| `seaborn` | Statistical data visualisation |

---

## Databases
| Library | Use |
|---------|-----|
| `sqlalchemy` | ORM + raw SQL for many databases |
| `pymongo` | MongoDB driver |
| `redis` | Redis client |

---

## Utilities
| Library | Use |
|---------|-----|
| `rich` | Beautiful terminal output |
| `click` | Command-line interface builder |
| `pydantic` | Data validation with type hints |
| `python-dotenv` | Load `.env` files |

---

## Quick Example — `rich`

```python
from rich import print
from rich.table import Table

table = Table(title="Score Board")
table.add_column("Name")
table.add_column("Score", justify="right")
table.add_row("Alice", "95")
table.add_row("Bob",   "82")
print(table)
```

---

## How to Discover Libraries

1. Search [PyPI](https://pypi.org) for the task keyword
2. Check download count and last-updated date
3. Read the README before installing

---

## Key Takeaways
- PyPI hosts 500k+ packages — most common tasks already have great libraries
- Check star count, recent activity, and licence before adopting a package
- Install in a virtual environment, then freeze to `requirements.txt`

---

## Exercises
See `exercises.py`

---

<!-- nav -->
[📝 Exercises](exercises.py) | [← Day 47](../Day47/lesson.md) | [Day 49 →](../Day49/lesson.md)
<!-- nav -->
