<!-- assignments-nav -->
[🏠 Home](../../) | [📚 Week 05 Lessons — Advanced Data Structures](../../Week05/)

---
<!-- assignments-nav -->

# Week 05 Assignments — Advanced Data Structures

**Days 29–35 · Topics: Stacks, Queues, Linked Lists, Sorting, Generators, Decorators**

---

## Assignments

### Day 29 — Stacks & Queues
- Implement a stack using a list and test push/pop/peek
- Implement a queue using `collections.deque` and test enqueue/dequeue
- Use a stack to evaluate a simple arithmetic expression like `3 4 + 2 *` (RPN)

### Day 30 — Linked Lists
- Implement a singly linked list with `append`, `prepend`, and `delete`
- Write a `reverse()` method for your linked list
- Detect a cycle in a linked list using the two-pointer (fast/slow) technique

### Day 31 — Sorting & Searching
- Implement bubble sort and time it against Python's built-in `sorted()`
- Implement binary search iteratively and recursively
- Write a function that returns the k-th largest element without fully sorting

### Day 32 — Nested Data Structures
- Parse a JSON response with deeply nested user/order/product data
- Write a `flatten_dict(d, sep=".")` function (e.g. `{"a": {"b": 1}}` → `{"a.b": 1}`)
- Group a list of transactions by user and calculate each user's total

### Day 33 — Generators & Iterators
- Write a `fibonacci_gen()` generator
- Write a `read_large_csv(path)` generator that yields one row at a time
- Write a `chunked(iterable, size)` generator that yields sublists of given size

### Day 34 — Decorators
- Write a `@timer` decorator that prints function execution time
- Write a `@retry(n)` decorator that retries a function up to n times on exception
- Write a `@memoize` decorator (without using `functools.lru_cache`)

### Day 35 — Project: Library Catalogue
- Add a search by author or partial title
- Add a checkout/return system with due dates
- Persist the catalogue to a JSON file

---

## Grading Criteria

| Criteria | Points |
|----------|--------|
| Implementation correctness | 40 |
| Efficient use of appropriate data structures | 30 |
| Edge cases handled | 20 |
| Code readability | 10 |
| **Total** | **100** |
