# nested_list_demo.py
# Working with nested lists

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]

print("Matrix:", matrix)
print("Element at row 2, column 3:", matrix[1][2])

# Iterating through nested list
for row in matrix:
    for item in row:
        print(item, end=" ")
    print()
