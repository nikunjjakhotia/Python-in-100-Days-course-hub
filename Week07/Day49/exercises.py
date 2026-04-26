# Day 49 – Project: Build a Reusable Utility Library
# Full pyutils package implemented in a single file for portability.
# In a real project, split into pyutils/strings.py, numbers.py, dates.py.

import re
from datetime import date, timedelta


# ─── strings module ──────────────────────────────────────────────────────────

def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")

def truncate(text: str, max_len: int, suffix: str = "...") -> str:
    if len(text) <= max_len:
        return text
    return text[:max_len - len(suffix)] + suffix

def word_count(text: str) -> dict:
    words = re.findall(r"[a-z']+", text.lower())
    counts = {}
    for w in words:
        counts[w] = counts.get(w, 0) + 1
    return counts


# ─── numbers module ──────────────────────────────────────────────────────────

def clamp(value: float, lo: float, hi: float) -> float:
    return max(lo, min(hi, value))

def percentage(part: float, total: float) -> float:
    return round(part / total * 100, 2) if total else 0.0

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


# ─── dates module ────────────────────────────────────────────────────────────

def days_until(target: date) -> int:
    return (target - date.today()).days

def date_range(start: date, end: date):
    current = start
    while current < end:
        yield current
        current += timedelta(days=1)

def friendly(d: date) -> str:
    return d.strftime("%A, %d %B %Y")


# ─── demo ────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    # strings
    print(slugify("Hello, World! This is Python."))
    print(truncate("The quick brown fox jumps over the lazy dog", 25))
    print(word_count("to be or not to be that is the question"))

    # numbers
    print(clamp(150, 0, 100))
    print(percentage(33, 200))
    primes = [n for n in range(2, 30) if is_prime(n)]
    print("Primes < 30:", primes)

    # dates
    christmas = date(date.today().year, 12, 25)
    print(f"Days until Christmas: {days_until(christmas)}")
    week = list(date_range(date.today(), date.today() + timedelta(days=7)))
    print("Next 7 days:", [str(d) for d in week])
    print(friendly(date.today()))
