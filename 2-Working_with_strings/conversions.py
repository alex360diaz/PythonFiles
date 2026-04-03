# Case Conversions

# lower() --> makes all letters lowercase
# Use Case - Standardize Text Case
text = "python PROGRAMMING"
print(text.lower())
# upper() --> makes all letters uppercase
print(text.upper())

#Use Case - Clean Data for Matching
search = "Email ".lower().strip()
data = " email".lower().strip()

print(search == data)