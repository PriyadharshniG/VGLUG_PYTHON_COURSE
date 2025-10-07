# break_continue_pass_demo.py
# Demonstrating break, continue, and pass

for i in range(1, 6):
    if i == 3:
        print("Skipping number 3")
        continue   # Skip iteration
    if i == 5:
        print("Stopping at 5")
        break      # Exit loop
    print("Number:", i)
else:
    # This else will not run because loop is broken
    print("Loop completed")
    
# Using pass
for i in range(3):
    pass  # Placeholder for future code
