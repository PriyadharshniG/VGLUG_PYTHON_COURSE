# duplicate_elements.py
# Find duplicates in a list

numbers = [1, 2, 3, 2, 5, 1, 6]
duplicates = set([x for x in numbers if numbers.count(x) > 1])
print("Duplicate elements:", duplicates)
