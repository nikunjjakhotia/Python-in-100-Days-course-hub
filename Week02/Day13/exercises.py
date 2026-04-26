# Day 13 – Mini Challenges: Control Flow Practice

# Exercise 1: FizzBuzz (1 to 100)
# Divisible by 3 → "Fizz", by 5 → "Buzz", by both → "FizzBuzz", else the number.

# Solution:
for i in range(1, 101):
    if i % 15 == 0:
        print("FizzBuzz", end=" ")
    elif i % 3 == 0:
        print("Fizz", end=" ")
    elif i % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(i, end=" ")
print()


# Exercise 2: Count vowels in a user-entered string.

# Solution:
sentence = input("Enter a sentence: ")
vowel_count = sum(1 for c in sentence if c in "aeiouAEIOU")
print(f"Vowel count: {vowel_count}")


# Exercise 3: Reverse a string without slicing — loop character by character.

# Solution:
word = input("Enter a word to reverse: ")
reversed_word = ""
for char in word:
    reversed_word = char + reversed_word
print(f"Reversed: {reversed_word}")


# Exercise 4: Find the largest number in a list without using max().

# Solution:
nums = [34, 7, 92, 15, 63, 41]
largest = nums[0]
for n in nums:
    if n > largest:
        largest = n
print(f"Largest: {largest}")


# Exercise 5: Print a right-angled triangle of stars where size is user input.
# Example for size=4:
# *
# * *
# * * *
# * * * *

# Solution:
size = int(input("Enter triangle size: "))
for row in range(1, size + 1):
    print("* " * row)
