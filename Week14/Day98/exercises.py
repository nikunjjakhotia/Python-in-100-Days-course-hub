# Day 98 – Interview Prep: OOP & Design Patterns

from abc import ABC, abstractmethod


# Exercise 1: Demonstrate encapsulation — BankAccount with private balance.

class BankAccount:
    def __init__(self, owner, balance=0.0):
        self.owner    = owner
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive.")
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Insufficient funds.")
        self.__balance -= amount

    def __str__(self):
        return f"BankAccount({self.owner}, balance=${self.__balance:.2f})"

acc = BankAccount("Alice", 100)
acc.deposit(50)
acc.withdraw(30)
print(acc)
try:
    acc.withdraw(500)
except ValueError as e:
    print("Expected error:", e)


# Exercise 2: Polymorphism — Shape hierarchy.

class Shape(ABC):
    @abstractmethod
    def area(self) -> float: ...
    @abstractmethod
    def perimeter(self) -> float: ...
    def describe(self):
        return f"{self.__class__.__name__}: area={self.area():.2f}, perimeter={self.perimeter():.2f}"

import math

class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self):      return math.pi * self.r ** 2
    def perimeter(self): return 2 * math.pi * self.r

class Rectangle(Shape):
    def __init__(self, w, h): self.w, self.h = w, h
    def area(self):      return self.w * self.h
    def perimeter(self): return 2 * (self.w + self.h)

shapes = [Circle(5), Rectangle(4, 6), Circle(3)]
for s in shapes:
    print(s.describe())


# Exercise 3: Singleton pattern.

class AppConfig:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.debug = False
            cls._instance.db_path = "app.db"
        return cls._instance

cfg1 = AppConfig()
cfg2 = AppConfig()
cfg1.debug = True
print("\nSingleton — same object?", cfg1 is cfg2)
print("cfg2.debug (set via cfg1):", cfg2.debug)


# Exercise 4: Factory pattern — create different report formats.

class TextReport:
    def render(self, data): return "\n".join(f"  {k}: {v}" for k, v in data.items())

class CSVReport:
    def render(self, data): return ",".join(data.keys()) + "\n" + ",".join(str(v) for v in data.values())

def make_report(fmt):
    return {"text": TextReport, "csv": CSVReport}[fmt]()

data = {"name": "Alice", "score": 95, "grade": "A"}
for fmt in ("text", "csv"):
    print(f"\n{fmt.upper()} report:")
    print(make_report(fmt).render(data))


# Exercise 5: Observer pattern.

class EventEmitter:
    def __init__(self):
        self._listeners = []
    def on(self, fn):
        self._listeners.append(fn)
    def emit(self, data):
        for fn in self._listeners:
            fn(data)

emitter = EventEmitter()
emitter.on(lambda d: print(f"\nListener A received: {d}"))
emitter.on(lambda d: print(f"Listener B received: {d}"))
emitter.emit({"event": "user_login", "user": "Alice"})
