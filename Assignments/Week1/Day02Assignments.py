# 🧠 Day 02 – Exercise: Variables and Data Types

## 🧪 Exercise 1: Swap Two Variables

'''
Write a Python program that swaps the values of two variables.
Example:

```python
a = 5
b = 10
# After swapping:
# a should be 10, b should be 5

'''
a = 5
b = 10
c=0

print ("Current values of a = ",a,"and b = ",b)

c=a
a=b
b=c

print ("Swapping is done. New values for a = ",a," and b = ",b)

'''
🧪 Exercise 2: Simple Calculator
Create variables x and y, assign any two numbers, and print their:

Addition

Subtraction

Multiplication

Division
'''

x=8
y=2

print("Addition =",x+y)
print("Subtraction =",x-y)
print("Multiplication =",x*y)
print("Division =",x/y)

'''
🧪 Exercise 3: Type Identification
Create one variable of each of the following data types and print their type using type():
Integer
Float
String
Boolean
'''

j=10
k=5.0
l="this is a text message"
m=True

print(type(j))
print(type(k))
print(type(l))
print(type(m))

'''
🧪 Bonus Exercise: Temperature Converter
Create a variable celsius and convert it to Fahrenheit using the formula:
fahrenheit = (celsius * 9/5) + 32
'''

celsius=26
fahrenheit=(celsius * 9/5) + 32

print("Celsius = ",celsius)
print("Fahrenheit = ",fahrenheit)

