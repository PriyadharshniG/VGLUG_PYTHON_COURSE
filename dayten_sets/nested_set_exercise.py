# nested_set_exercise.py
# Practice exercises with sets

# 1. Remove duplicates from a list using set
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
print("Unique numbers:", unique_numbers)

# 2. Find common elements between two lists
list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]
common = set(list1) & set(list2)
print("Common elements:", common)

# 3. Find elements in list1 not in list2
diff = set(list1) - set(list2)
print("Elements in list1 not in list2:", diff)
