# Day 23 – Custom Exceptions

# Exercise 1: Create NegativeNumberError and raise it if a number is negative.

# Solution:
class NegativeNumberError(Exception):
    pass

def square_root(n):
    if n < 0:
        raise NegativeNumberError(f"Cannot take square root of {n}")
    return n ** 0.5

try:
    print(square_root(16))
    print(square_root(-4))
except NegativeNumberError as e:
    print(f"Error: {e}")


# Exercise 2: Create InsufficientFundsError for a simple bank account.

# Solution:
class InsufficientFundsError(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientFundsError(
            f"Cannot withdraw ${amount:.2f}. Available: ${balance:.2f}"
        )
    return balance - amount

try:
    bal = 200.0
    bal = withdraw(bal, 50)
    print(f"Withdrawal successful. New balance: ${bal:.2f}")
    bal = withdraw(bal, 300)
except InsufficientFundsError as e:
    print(f"Transaction failed: {e}")


# Exercise 3: Create an InvalidAgeError with a custom attribute.

# Solution:
class InvalidAgeError(Exception):
    def __init__(self, age):
        self.age = age
        super().__init__(f"Age {age} is not valid (must be 0-120)")

def register_user(age):
    if not (0 <= age <= 120):
        raise InvalidAgeError(age)
    return f"User registered with age {age}"

for test_age in [25, -1, 150]:
    try:
        print(register_user(test_age))
    except InvalidAgeError as e:
        print(f"Registration failed: {e}")


# Exercise 4: Build a small exception hierarchy: AppError > DatabaseError, NetworkError.

# Solution:
class AppError(Exception): pass
class DatabaseError(AppError): pass
class NetworkError(AppError): pass

def simulate(error_type):
    if error_type == "db":
        raise DatabaseError("Could not connect to database")
    elif error_type == "net":
        raise NetworkError("Network timeout")

for t in ["db", "net"]:
    try:
        simulate(t)
    except AppError as e:
        print(f"App error caught: {type(e).__name__}: {e}")


# Exercise 5: Re-raise an exception after logging it.

# Solution:
def risky():
    raise ValueError("Something went wrong internally")

try:
    try:
        risky()
    except ValueError as e:
        print(f"Logged: {e}")
        raise
except ValueError:
    print("Outer handler: error was re-raised and caught here.")
