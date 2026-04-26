# Day 37 – Instance vs Class Variables

# Exercise 1: Use a class variable to track how many Employee objects are created.

# Solution:
class Employee:
    headcount = 0

    def __init__(self, name, department):
        self.name = name
        self.department = department
        Employee.headcount += 1

e1 = Employee("Alice", "Engineering")
e2 = Employee("Bob", "Marketing")
e3 = Employee("Charlie", "Data")
print(f"Employees created: {Employee.headcount}")


# Exercise 2: Add a @classmethod that creates an Employee from a "name:dept" string.

# Solution:
class Employee2:
    headcount = 0

    def __init__(self, name, department):
        self.name = name
        self.department = department
        Employee2.headcount += 1

    @classmethod
    def from_string(cls, s):
        name, dept = s.split(":")
        return cls(name.strip(), dept.strip())

    def __str__(self):
        return f"{self.name} ({self.department})"

e = Employee2.from_string("Diana : Data Science")
print(e)
print(f"Total: {Employee2.headcount}")


# Exercise 3: Add a @staticmethod to validate if a salary is reasonable (> 0 and < 1_000_000).

# Solution:
class SalaryManager:
    @staticmethod
    def is_valid_salary(salary):
        return 0 < salary < 1_000_000

print(SalaryManager.is_valid_salary(75000))   # True
print(SalaryManager.is_valid_salary(-5000))   # False
print(SalaryManager.is_valid_salary(2000000)) # False


# Exercise 4: Show that a class variable shared as a list can cause surprises.

# Solution:
class BuggyClass:
    shared_list = []   # shared — ALL instances see changes!

    def add(self, item):
        self.shared_list.append(item)

a = BuggyClass()
b = BuggyClass()
a.add("from a")
print(b.shared_list)  # ['from a'] — b sees it too!

class FixedClass:
    def __init__(self):
        self.my_list = []  # each instance gets its own list

    def add(self, item):
        self.my_list.append(item)

x = FixedClass()
y = FixedClass()
x.add("from x")
print(y.my_list)  # [] — y is unaffected
