# Day 10 – While Loops

# Exercise 1: Count from 1 to 10 using a while loop.

# Solution:
count = 1
while count <= 10:
    print(count, end=" ")
    count += 1
print()


# Exercise 2: Sum all numbers from 1 to 100.

# Solution:
total = 0
n = 1
while n <= 100:
    total += n
    n += 1
print(f"Sum 1-100: {total}")


# Exercise 3: Input validation — keep asking until the user enters a positive number.

# Solution:
while True:
    num = int(input("Enter a positive number: "))
    if num > 0:
        print(f"Thanks! You entered: {num}")
        break
    print("That's not positive. Try again.")


# Exercise 4: Guess the number game (number is fixed at 7).
# Keep prompting until the user guesses correctly.

# Solution:
secret = 7
while True:
    guess = int(input("Guess the number (1-10): "))
    if guess == secret:
        print("Correct!")
        break
    elif guess < secret:
        print("Too low!")
    else:
        print("Too high!")


# Exercise 5: Print all even numbers between 1 and 20 using continue.

# Solution:
i = 0
while i < 20:
    i += 1
    if i % 2 != 0:
        continue
    print(i, end=" ")
print()
