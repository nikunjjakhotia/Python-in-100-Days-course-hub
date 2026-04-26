# Day 48 – Popular Third-Party Libraries


# Exercise 1: Install `rich` (pip install rich), then use it to print a coloured
# welcome banner and a simple table of your favourite programming languages.

# Solution (run after: pip install rich):
try:
    from rich.console import Console
    from rich.table import Table

    console = Console()
    console.print("[bold green]Welcome to Python Day 48![/bold green]")

    table = Table(title="Favourite Languages")
    table.add_column("Language", style="cyan")
    table.add_column("Paradigm")
    table.add_column("Year", justify="right")
    table.add_row("Python",     "Multi-paradigm",  "1991")
    table.add_row("JavaScript", "Event-driven",    "1995")
    table.add_row("Rust",       "Systems",         "2010")
    console.print(table)
except ImportError:
    print("Install rich first: pip install rich")


# Exercise 2: Install `python-dotenv` (pip install python-dotenv).
# Create a file called `.env` with: SECRET_KEY=abc123
# Then load it and print the value of SECRET_KEY.

# Solution:
try:
    from dotenv import load_dotenv
    import os

    # create a demo .env file if it doesn't exist
    if not os.path.exists(".env"):
        with open(".env", "w") as f:
            f.write("SECRET_KEY=abc123\n")

    load_dotenv()
    print("SECRET_KEY:", os.getenv("SECRET_KEY"))
except ImportError:
    print("Install python-dotenv first: pip install python-dotenv")


# Exercise 3: Use only the standard library to simulate what `pydantic` validates:
# write a `validate_user(data: dict)` that raises ValueError if "name" or "age" are missing
# or if age is not an integer >= 0.

def validate_user(data):
    if "name" not in data:
        raise ValueError("Missing 'name'")
    if "age" not in data:
        raise ValueError("Missing 'age'")
    if not isinstance(data["age"], int) or data["age"] < 0:
        raise ValueError("'age' must be a non-negative integer")
    return data

print(validate_user({"name": "Alice", "age": 30}))
try:
    validate_user({"name": "Bob", "age": -5})
except ValueError as e:
    print(e)
