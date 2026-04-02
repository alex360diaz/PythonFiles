# Removing spaces
# lstrip() --> removes spaces from the left side of a string
text = " Engineering"
print(text)
print(text.lstrip())
print("-"*20)

# rstrip() --> removes spaces from the right side of a string
text2 = "Engineering "
print(text2)
print("Lenght of the string:" , len(text2))
print(text2.rstrip())
print("Lenght of the string:" , len(text2.rstrip()))
print("-"*20)

# strip() --> removes spaces from the left and right side of a string
text3 = "     Engineering "
print(text3)
print("Lenght of the string:" , len(text3))
print(text3.strip())
print("Lenght of the string:" , len(text3.strip()))
print("-"*20)

# No only is for spaces also for characters
text3 = "-----Engineering---"
print(text3)
print(text3.strip("-"))
print("-"*20)

#USE CASE - Detect Extra Spaces
text4 = input("Type somenthig:")
count_white = len(text4)
count_str = len(text4.strip())

if count_white > count_str :
    print("You have spaces in the string")
else:
    print("No white spaces in the string")

