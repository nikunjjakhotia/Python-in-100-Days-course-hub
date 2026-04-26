# Day 04 – Lists & Indexing

# Exercise 1: Create a list of 5 favorite things; print first, last, and middle items.

# Solution:
favorites = ["pizza", "swimming", "Python", "travel", "music"]
print("First:", favorites[0])
print("Last:", favorites[-1])
print("Middle:", favorites[len(favorites) // 2])


# Exercise 2: List slicing on a cities list.

# Solution:
cities = ["Montreal", "Toronto", "Vancouver", "Calgary", "Ottawa"]
print("First three:", cities[:3])
print("Last two:", cities[-2:])
print("Total cities:", len(cities))


# Exercise 3: Modify a list — append, remove, and sort.

# Solution:
numbers = [42, 7, 13, 99, 5]
numbers.append(25)
numbers.remove(13)
numbers.sort()
print("Modified list:", numbers)


# Exercise 4: Use list methods — count and index.

# Solution:
letters = ["a", "b", "c", "a", "d", "a"]
print("Count of 'a':", letters.count("a"))
print("Index of 'c':", letters.index("c"))


# Exercise 5: Reverse a list without using .reverse().

# Solution:
nums = [1, 2, 3, 4, 5]
reversed_nums = nums[::-1]
print("Reversed:", reversed_nums)
