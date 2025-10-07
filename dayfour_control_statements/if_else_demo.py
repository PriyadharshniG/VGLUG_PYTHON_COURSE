# if_else_demo.py
# Demonstrating if, elif, else statements

age = int(input("Enter your age: "))

if age < 18:
    print("You are a minor.")
elif age >= 18 and age < 60:
    print("You are an adult.")
else:
    print("You are a senior citizen.")
