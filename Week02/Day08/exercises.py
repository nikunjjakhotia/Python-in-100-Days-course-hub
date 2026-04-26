# Day 08 – if / elif / else

# Exercise 1: Age classifier
# Ask for age and print: "Child" (<13), "Teenager" (13-17), "Adult" (18-64), "Senior" (65+)

# Solution:
age = int(input("Enter your age: "))
if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
elif age < 65:
    print("Adult")
else:
    print("Senior")


# Exercise 2: Grade calculator
# Score 90+ = A, 80+ = B, 70+ = C, 60+ = D, below = F

# Solution:
score = int(input("Enter your score (0-100): "))
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(f"Grade: {grade}")


# Exercise 3: Even or Odd checker

# Solution:
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is Even")
else:
    print(f"{num} is Odd")


# Exercise 4: Login simulator — check username AND password

# Solution:
correct_user = "admin"
correct_pass = "python123"
username = input("Username: ")
password = input("Password: ")
if username == correct_user and password == correct_pass:
    print("Login successful!")
else:
    print("Invalid credentials.")


# Exercise 5: Largest of three numbers

# Solution:
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a >= b and a >= c:
    print(f"Largest: {a}")
elif b >= a and b >= c:
    print(f"Largest: {b}")
else:
    print(f"Largest: {c}")
