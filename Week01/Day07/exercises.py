# Day 07 – Project: My Bio App
# Combines: variables, input(), type casting, f-strings

# ----- Project: Bio App -----

print("=" * 42)
print("       WELCOME TO YOUR BIO APP")
print("=" * 42)

name = input("Enter your full name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")
hobby = input("Enter your favorite hobby: ")
fun_fact = input("Share a fun fact about yourself: ")
fav_number = int(input("Enter your favorite number: "))

birth_year = 2025 - age
doubled = fav_number * 2

print("\n" + "╔" + "═" * 40 + "╗")
print("           MY BIO CARD")
print("╚" + "═" * 40 + "╝")
print(f"  Name      : {name}")
print(f"  Age       : {age}  (Born ~{birth_year})")
print(f"  City      : {city}")
print(f"  Hobby     : {hobby}")
print(f"  Fun Fact  : {fun_fact}")
print(f"  Lucky #   : {fav_number}  →  Doubled: {doubled}")
print("=" * 42)


# ----- Bonus: second hobby -----
# hobby2 = input("Enter a second hobby: ")
# print(f"Hobbies: {hobby} and {hobby2}")
