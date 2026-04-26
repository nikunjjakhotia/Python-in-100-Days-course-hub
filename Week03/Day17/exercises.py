# Day 17 – Scope

# Exercise 1: Demonstrate that a local variable can't be accessed outside its function.

# Solution:
def create_local():
    local_var = "I'm local"
    print(local_var)

create_local()
# print(local_var)  # Uncommenting raises NameError


# Exercise 2: Read a global variable inside a function (no modification).

# Solution:
greeting = "Hello from global scope"

def read_global():
    print(greeting)

read_global()


# Exercise 3: Use 'global' to modify a counter from inside a function.
# Call increment() 3 times and print the final counter.

# Solution:
visits = 0

def increment():
    global visits
    visits += 1

increment()
increment()
increment()
print(f"Total visits: {visits}")  # 3


# Exercise 4: Demonstrate variable shadowing — local variable hides global.

# Solution:
x = "global x"

def shadow():
    x = "local x"   # shadows the global
    print(x)

shadow()
print(x)   # still "global x"


# Exercise 5: Use nonlocal inside a nested function to build a simple counter closure.

# Solution:
def make_counter():
    count = 0
    def tick():
        nonlocal count
        count += 1
        return count
    return tick

counter = make_counter()
print(counter())  # 1
print(counter())  # 2
print(counter())  # 3
