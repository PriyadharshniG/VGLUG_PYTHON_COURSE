# identity_operators.py
# Identity Operators Example

x = [1, 2, 3]
y = [1, 2, 3]
z = x

print("x is z:", x is z)   # True
print("x is y:", x is y)   # False
print("x == y:", x == y)   # True (values are equal)

# Using in conditional
if x is not y:
    print("x and y are not the same object in memory")
