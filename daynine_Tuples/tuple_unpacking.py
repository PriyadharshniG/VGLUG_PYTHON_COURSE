# tuple_unpacking.py
# Unpacking tuples

point = (10, 20)
x, y = point
print("x:", x)
print("y:", y)

# Unpacking with *
numbers = (1, 2, 3, 4, 5)
first, *middle, last = numbers
print("First:", first)
print("Middle:", middle)
print("Last:", last)
