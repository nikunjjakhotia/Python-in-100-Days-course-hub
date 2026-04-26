# Day 46 – Packages & __init__.py
# These exercises simulate how a package is structured; code is self-contained here.


# Exercise 1: Simulate a package structure by writing three "module" sections.
# --- strings module ---
def slugify(text):
    import re
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")

def truncate(text, max_len, suffix="..."):
    if len(text) <= max_len:
        return text
    return text[:max_len - len(suffix)] + suffix

# --- numbers module ---
def clamp(value, lo, hi):
    return max(lo, min(hi, value))

def percentage(part, total):
    return round(part / total * 100, 2) if total else 0.0

# --- package __init__ would re-export these ---

print(slugify("Hello World! This is Python."))
print(truncate("The quick brown fox jumps over the lazy dog", 20))
print(clamp(150, 0, 100))
print(percentage(45, 200))


# Exercise 2: Show how __init__.py re-exports work by creating a dict that acts
# as a "namespace" and pulling in functions from the two "modules" above.

pyutils = {
    "slugify":    slugify,
    "truncate":   truncate,
    "clamp":      clamp,
    "percentage": percentage,
}

# caller code:
print(pyutils["slugify"]("  My Package Name!  "))
print(pyutils["percentage"](33, 50))


# Exercise 3: Demonstrate relative-import naming convention by printing
# the __name__ of this file and explaining what it would be inside a package.

print(__name__)
# When this file IS a module inside a package, __name__ == "package.module"
# relative import: from .numbers import clamp  (same package)
# absolute import: from mypackage.numbers import clamp


# Exercise 4: Write a function `list_public_names(module_dict)` that returns
# only names not starting with "_", mimicking what `dir(module)` filtered output does.

def list_public_names(namespace):
    return [k for k in namespace if not k.startswith("_")]

print(list_public_names(pyutils))
