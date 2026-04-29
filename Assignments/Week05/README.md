<!-- assignments-nav -->
[🏠 Home](../../) | [📚 Week 05 Lessons — Advanced Data Structures](../../Week05/)

---
<!-- assignments-nav -->

# Week 05 Assignment: Build a Task Queue Manager

**Days 29–35 · Topics: Stacks, Queues, Linked Lists, Sorting, Generators, Decorators**

Using the data structures and patterns from Days 29–35, build a CLI task manager backed by a priority queue, with generator-powered output and decorator-based logging.

## What to Build
- A `TaskQueue` class using `collections.deque` with `enqueue`, `dequeue`, and `peek` methods
- A priority field (1–3) that determines task order, sorted on each enqueue
- A `pending_tasks()` generator that yields tasks one at a time without loading them all into memory
- A `@log_call` decorator that prints the function name and a timestamp on every queue operation
- A `@timer` decorator that measures how long `sort_tasks()` takes — compare it against Python's `sorted()`
