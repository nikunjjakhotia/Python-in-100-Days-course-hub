# Week 03 Assignments — Functions

**Days 15–21 · Topics: Function Definition, Parameters, *args/**kwargs, Scope, Lambda, Recursion**

---

## Assignments

### Day 15 — Defining & Calling Functions
- Write a `greet(name, greeting="Hello")` function
- Write a `celsius_to_fahrenheit(c)` and `fahrenheit_to_celsius(f)` pair
- Write a `is_even(n)` function and use it to filter a list

### Day 16 — Parameters, Arguments & Defaults
- Write a `create_profile(name, age, city="Unknown", job="Unemployed")` function
- Write `format_price(amount, currency="USD", decimals=2)` 
- Write a `clamp(value, lo=0, hi=100)` function

### Day 17 — *args & **kwargs
- Write `sum_all(*numbers)` that sums any number of arguments
- Write `print_info(**details)` that prints each key-value pair
- Combine both: `describe(*features, **specs)` that formats a product description

### Day 18 — Scope & Variable Lifetime
- Explain (with code examples) why modifying a global variable inside a function is bad practice
- Demonstrate the difference between mutable and immutable default arguments
- Write a counter using a closure (return a function that increments a counter)

### Day 19 — Lambda & Higher-Order Functions
- Sort a list of dicts by a given key using a lambda
- Use `map()` to double all numbers in a list
- Use `filter()` to keep only strings longer than 5 characters
- Chain `map` and `filter` to square all even numbers in a list

### Day 20 — Recursion
- Write a recursive `power(base, exp)` function
- Write a recursive `flatten(nested_list)` function
- Write recursive binary search

### Day 21 — Project: Calculator & Unit Converter
- Add a history feature that stores the last 10 calculations
- Add percentage and square-root operations
- Extend unit converter with length, weight, and temperature

---

## Grading Criteria

| Criteria | Points |
|----------|--------|
| Correct output | 40 |
| Uses the day's concepts (not brute-forced) | 30 |
| Edge cases handled | 20 |
| Clean function signatures with type hints | 10 |
| **Total** | **100** |
