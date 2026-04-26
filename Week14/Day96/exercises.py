# Day 96 – Interview Prep: Data Structures

from collections import deque, Counter, defaultdict


# Exercise 1: Two Sum — return indices of the two numbers that add to target.

def two_sum(nums, target):
    seen = {}
    for i, n in enumerate(nums):
        complement = target - n
        if complement in seen:
            return [seen[complement], i]
        seen[n] = i
    return []

print("two_sum([2,7,11,15], 9):", two_sum([2, 7, 11, 15], 9))    # [0, 1]
print("two_sum([3,2,4], 6):",    two_sum([3, 2, 4], 6))           # [1, 2]


# Exercise 2: Valid brackets — return True if brackets are balanced.

def is_valid(s):
    stack = []
    pairs = {")": "(", "}": "{", "]": "["}
    for ch in s:
        if ch in "([{":
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack[-1] != pairs[ch]:
                return False
            stack.pop()
    return not stack

for s in ["()", "()[]{}", "(]", "([)]", "{[]}"]:
    print(f"is_valid('{s}'): {is_valid(s)}")


# Exercise 3: Sliding window maximum sum of k consecutive elements.

def max_subarray_sum(nums, k):
    window = sum(nums[:k])
    best   = window
    for i in range(k, len(nums)):
        window += nums[i] - nums[i - k]
        best = max(best, window)
    return best

print("\nmax_subarray_sum([2,3,4,1,5], 3):", max_subarray_sum([2, 3, 4, 1, 5], 3))  # 9


# Exercise 4: Group anagrams together.

def group_anagrams(words):
    groups = defaultdict(list)
    for w in words:
        key = tuple(sorted(w))
        groups[key].append(w)
    return list(groups.values())

print("\ngroup_anagrams:", group_anagrams(["eat","tea","tan","ate","nat","bat"]))


# Exercise 5: Use a deque to implement a simple queue (FIFO).

q = deque()
for item in ["task1", "task2", "task3"]:
    q.append(item)        # enqueue
print("\nQueue:", list(q))
print("Dequeued:", q.popleft())   # task1
print("Queue after pop:", list(q))


# Exercise 6: Find the most common word in a sentence.

sentence = "to be or not to be that is the question to be"
word = Counter(sentence.split()).most_common(1)[0]
print(f"\nMost common word: '{word[0]}' ({word[1]} times)")
