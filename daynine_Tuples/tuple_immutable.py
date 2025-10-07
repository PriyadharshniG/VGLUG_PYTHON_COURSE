# tuple_immutable.py
# Demonstrating immutability of tuples

t = (1, 2, 3)

try:
    t[0] = 10
except TypeError as e:
    print("Error:", e)

# But we can concatenate or create new tuples
t2 = t + (4, 5)
print("Original tuple:", t)
print("New tuple after concatenation:", t2)
