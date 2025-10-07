# string_exercise.py
# Practice exercises

text = input("Enter a sentence: ")

# 1. Count words
word_count = len(text.split())
print("Word count:", word_count)

# 2. Reverse string
print("Reversed:", text[::-1])

# 3. Replace vowels with '*'
vowels = "aeiouAEIOU"
replaced = "".join(["*" if ch in vowels else ch for ch in text])
print("Vowels replaced:", replaced)
