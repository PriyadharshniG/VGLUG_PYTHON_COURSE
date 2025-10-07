# identity_membership.py
# Demonstrating identity and membership operators

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print("x is z:", x is z)
print("x is y:", x is y)
print("x == y:", x == y)

fruits = ["apple", "mango", "orange"]
print("'mango' in fruits:", "mango" in fruits)
print("'grape' not in fruits:", "grape" not in fruits)
