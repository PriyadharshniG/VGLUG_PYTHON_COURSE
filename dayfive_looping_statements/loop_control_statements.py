# loop_control_statements.py
# Using break, continue, and pass in loops

for i in range(1, 6):
    if i == 3:
        print("Skipping number 3")
        continue   # Skip this iteration
    if i == 5:
        print("Stopping at 5")
        break      # Exit the loop
    print("Number:", i)


for i in range(3):
    pass  
