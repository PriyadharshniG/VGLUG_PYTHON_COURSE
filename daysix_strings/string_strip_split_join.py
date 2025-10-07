# string_strip_split_join.py
# Strip, split, join

text = "   VGLUG Python   "
print("Original:", text)
print("Strip spaces:", text.strip())

# Split
words = text.split()
print("Split words:", words)

# Join
joined_text = "-".join(words)
print("Joined with '-':", joined_text)
