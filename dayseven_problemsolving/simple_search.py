# simple_search.py
# Search for an element in a list

numbers = [5, 12, 7, 9, 20]
target = int(input("Enter number to search: "))

if target in numbers:
    print(target, "found in list")
else:
    print(target, "not found in list")
