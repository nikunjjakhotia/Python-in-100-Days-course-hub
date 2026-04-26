# Day 13 – Mini Challenges: Control Flow Practice

## Learning Objectives
- Solidify `if/elif/else`, `while`, and `for` with mixed challenges
- Think through algorithm logic before coding
- Practice translating plain-English rules into Python conditions

---

## Challenge 1: FizzBuzz

The classic coding interview warm-up.

```python
for i in range(1, 101):
    if i % 15 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)
```

> Tip: Check `% 15` first, otherwise `% 3` and `% 5` will match numbers divisible by both.

---

## Challenge 2: Find All Even Numbers in a List

```python
numbers = [4, 7, 12, 3, 8, 19, 22]
evens = []
for n in numbers:
    if n % 2 == 0:
        evens.append(n)
print(evens)
```

---

## Challenge 3: Count Vowels in a String

```python
sentence = input("Enter a sentence: ")
vowels = "aeiouAEIOU"
count = 0
for char in sentence:
    if char in vowels:
        count += 1
print(f"Vowel count: {count}")
```

---

## Challenge 4: Reverse a String Without Slicing

```python
word = input("Enter a word: ")
reversed_word = ""
for char in word:
    reversed_word = char + reversed_word
print(reversed_word)
```

---

## Key Takeaways
- Always test your conditions with edge cases (0, negatives, empty strings)
- `in` keyword works for membership testing on strings and lists
- Building up a result string or list inside a loop is a core pattern

---

## Exercises
See `exercises.py`
