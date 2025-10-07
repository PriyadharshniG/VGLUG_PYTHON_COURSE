# list_methods_demo.py
# Common list methods

numbers = [1, 2, 3, 4, 5]

numbers.append(6)
print("After append:", numbers)

numbers.insert(2, 10)
print("After insert at index 2:", numbers)

numbers.remove(4)
print("After remove 4:", numbers)

popped = numbers.pop()
print("After pop:", numbers, "Popped element:", popped)

numbers.extend([7, 8, 9])
print("After extend:", numbers)

print("Index of 10:", numbers.index(10))
print("Count of 2:", numbers.count(2))

numbers.sort()
print("Sorted list:", numbers)

numbers.reverse()
print("Reversed list:", numbers)
