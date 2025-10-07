# nested_if_demo.py
# Nested if statements example

num = int(input("Enter a number: "))

if num > 0:
    if num % 2 == 0:
        print("Positive even number")
    else:
        print("Positive odd number")
else:
    print("Number is zero or negative")
