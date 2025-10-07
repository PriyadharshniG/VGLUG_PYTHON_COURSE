# set_methods_demo.py
# Common set methods

numbers = {1, 2, 3, 4, 5}

# Adding elements
numbers.add(6)
print("After add:", numbers)

# Updating set with multiple elements
numbers.update([7, 8, 9])
print("After update:", numbers)

# Removing elements
numbers.remove(3)  # Raises KeyError if not found
print("After remove 3:", numbers)

numbers.discard(10)  # No error if not found
print("After discard 10:", numbers)

# Pop removes a random element
popped = numbers.pop()
print("After pop:", numbers, "Popped element:", popped)

# Clear set
temp_set = {1, 2, 3}
temp_set.clear()
print("After clear:", temp_set)
