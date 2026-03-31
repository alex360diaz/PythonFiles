# Math
#   len(value) --> returns the number of items in a value
#                  returns tje number of characters in a string
password = "123dsadfasda"
print(len(password))

if len(password) < 8:
    print("Your Password is too short")
else:
    print("Your Password it's fine")

# Math 2.0
#   count(substring) --> returns how often a word appears in the string
text = """
Python is easy learn.
Python is powerful.
Many people love python.
"""
print(text.count("Python")) #is case-sensitive: means uppercase and lowercase letters are treated as different
