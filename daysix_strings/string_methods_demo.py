# string_methods_demo.py
# Common string methods

name = "Priyadharshni"
greeting = "Hello World!"

print("Length of name:", len(name))
print("Uppercase:", name.upper())
print("Lowercase:", name.lower())
print("Title Case:", greeting.title())
print("Capitalize:", greeting.capitalize())
print("Swapcase:", greeting.swapcase())
print("Replace text:", greeting.replace("World", "VGLUG"))
print("Is alphabetic?", name.isalpha())
print("Is numeric?", "123".isnumeric())
print("Split string:", greeting.split())
print("Join strings:", "-".join(["VGLUG", "Python"]))