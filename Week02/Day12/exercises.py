# Day 12 – range() & Loop Control

# Exercise 1: Print all multiples of 3 between 1 and 50.

# Solution:
for i in range(3, 51, 3):
    print(i, end=" ")
print()


# Exercise 2: Countdown from 10 to 1, then print "Blast off!".

# Solution:
for i in range(10, 0, -1):
    print(i, end=" ")
print("\nBlast off!")


# Exercise 3: Print a 5x5 star grid using nested loops.

# Solution:
for row in range(5):
    for col in range(5):
        print("*", end=" ")
    print()


# Exercise 4: Use for...else to check if a number is prime.

# Solution:
num = int(input("Enter a number to check if it's prime: "))
for factor in range(2, int(num ** 0.5) + 1):
    if num % factor == 0:
        print(f"{num} is NOT prime (divisible by {factor})")
        break
else:
    print(f"{num} is PRIME")


# Exercise 5: Print the multiplication table (1–5) using nested loops.

# Solution:
for i in range(1, 6):
    for j in range(1, 6):
        print(f"{i * j:3}", end="")
    print()
