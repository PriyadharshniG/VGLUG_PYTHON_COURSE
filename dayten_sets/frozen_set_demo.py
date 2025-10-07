# frozen_set_demo.py
# Demonstrating frozenset (immutable set)

fs = frozenset([1, 2, 3, 4])
print("Frozen set:", fs)

try:
    fs.add(5)
except AttributeError as e:
    print("Error:", e)
