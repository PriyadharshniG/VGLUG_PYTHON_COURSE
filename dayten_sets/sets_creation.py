# set_creation.py
# Creating sets in Python

# Empty set (note: {} creates a dictionary)
empty_set = set()
print("Empty set:", empty_set)

# Set of integers
numbers = {1, 2, 3, 4, 5}
print("Numbers set:", numbers)

# Set of strings
fruits = {"apple", "banana", "mango"}
print("Fruits set:", fruits)

# Mixed data types
mixed = {1, "apple", 3.5, True}
print("Mixed set:", mixed)

# Duplicate elements are automatically removed
duplicates = {1, 2, 2, 3, 3, 3}
print("Set with duplicates removed:", duplicates)
