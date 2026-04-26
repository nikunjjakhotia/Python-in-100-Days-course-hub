# Day 97 – Interview Prep: Algorithms

from functools import lru_cache


# Exercise 1: Binary search — return index or -1.

def binary_search(arr, target):
    lo, hi = 0, len(arr) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1

nums = [1, 3, 5, 7, 9, 11, 13, 15]
print("binary_search for 7:",  binary_search(nums, 7))    # 3
print("binary_search for 6:",  binary_search(nums, 6))    # -1
print("binary_search for 15:", binary_search(nums, 15))   # 7


# Exercise 2: Fibonacci with memoisation.

@lru_cache(maxsize=None)
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print("\nfib(10):", fib(10))    # 55
print("fib(50):", fib(50))     # 12586269025 (instant with memoisation)


# Exercise 3: Merge sort.

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid   = len(arr) // 2
    left  = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j  = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

print("\nmerge_sort:", merge_sort([5, 2, 8, 1, 9, 3]))


# Exercise 4: Find duplicates in a list using a set (O(n)).

def find_duplicates(nums):
    seen, dups = set(), set()
    for n in nums:
        if n in seen:
            dups.add(n)
        seen.add(n)
    return sorted(dups)

print("\nfind_duplicates:", find_duplicates([1, 2, 3, 2, 4, 3, 5]))  # [2, 3]


# Exercise 5: Reverse words in a sentence.

def reverse_words(s):
    return " ".join(s.split()[::-1])

print("\nreverse_words:", reverse_words("Hello World from Python"))


# Exercise 6: Check if a string is a palindrome (ignore spaces & case).

import re

def is_palindrome(s):
    cleaned = re.sub(r"[^a-z0-9]", "", s.lower())
    return cleaned == cleaned[::-1]

for phrase in ["racecar", "A man a plan a canal Panama", "hello"]:
    print(f"is_palindrome('{phrase}'): {is_palindrome(phrase)}")
