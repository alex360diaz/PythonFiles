# Transformations
#   replace(old, new) : swaps part of the text with something new
# Example 1 : We we need to change de , for . becouse europe use , for decimals and other parts use . for decimals
price = "33,55"
print("Example 1")
print(price.replace(",", "."))

# Example 2 When user type their phone number like 0155/3234/56 intead of -
phone = "101/3455/67"
print("\nExample 2")
print(phone.replace("/", "-"))
# Also intead of insrting something new we can removed character for a clean number
print(phone.replace("/", ""))

# Example 3 to convert a string price to a float price
cost = "$1,299.99"
print("\nExample 3")
print(cost.replace("$", "").replace(",", ""))

# Example 4
# Replace the two first occurrence of the word "one":
txt = "one one was a race horse, two two was one too."
x = txt.replace("one", "three", 2)
print("\nExample 4")
print(x)

# Challenge
# Convert the messy phone number into a clean number format with only digits
#           "+49 (176) 123-4567"
messy_number = "+49 (176) 123-4567"
print("\nChallenge")
print(messy_number.replace("+", "").replace("(", "").replace(")",
      "").replace("-", "").replace(" ", ""))

#   'strting1" + 'string2' --> joins (concatinates) two strings into one.
first_name = "Alejandro"
last_name = "Diaz"
full_name = first_name + " " + last_name
print("\nSExample how to join strings")
print(full_name)
