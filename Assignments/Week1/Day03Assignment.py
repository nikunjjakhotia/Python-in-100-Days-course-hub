'''
## 🔢 Exercise 1: Calculator with Two Numbers

Ask the user to input two numbers and display the results of:
- Addition
- Subtraction
- Multiplication
- Division
'''

a=int(input("Please enter the 1st number: "))
b=int(input("Please enter the 2nd number: "))
print("Addition = ",a+b)
print("Subtraction = ",a-b)
print("Multiplication = ",a*b)
print("Division = ",a/b)

'''
## 🔤 Exercise 2: String Formatter

Take a user's name and favorite hobby as input. Display a sentence like:

```
Hi Nikunj! It's great that you love swimming.
```
'''
name=input("Enter your Name: ")
hobby=input("Enter your favorite hobby: ")
print("Hey",name,"! Its great that you love",hobby,".")

'''
## 🧮 Exercise 3: Tip Calculator (Bonus)

Ask the user for:
- Total bill amount (e.g., 100)
- Tip percentage they want to give (e.g., 15%)
- Number of people splitting the bill

Then calculate how much each person should pay.
'''

bill=float(input("Enter bill amount: "))
tip=float(input("Enter tip %: "))
people=int(input("Enter number of people splitting the bill: "))
tipamt=(tip*bill)/100
totalamt=bill+tipamt
splitup=totalamt/people
print("The Bill amount is:",bill)
print("The Tip % is:",tip)
print("The Tip amount is:",tipamt)
print("The Total amount is:",totalamt)
print("The splitup amount is:",splitup)


