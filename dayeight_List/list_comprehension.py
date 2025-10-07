# list_comprehension.py
# Using list comprehensions

# Squares of numbers 1-5
squares = [x**2 for x in range(1, 6)]
print("Squares:", squares)

# Even numbers from 1-10
evens = [x for x in range(1, 11) if x % 2 == 0]
print("Even numbers:", evens)

# Convert strings to uppercase
fruits = ["apple", "banana", "mango"]
upper_fruits = [f.upper() for f in fruits]
print("Uppercase fruits:", upper_fruits)
