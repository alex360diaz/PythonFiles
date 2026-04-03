# Search
# startswith() --> checks if the string begins with a specific word
# Is the phone code from Mexico?
phone = "+52-176-12345"
print(phone)
print("Is the phne code from Mexico:", phone.startswith("+52"))
print("-"*44)
# endswith() --> checks if the string ends with a specific word
# Is the emial from gmail?
emial = "diaz360arteaga@gmail.com"
print(emial)
print("Is the emial from gmail?:", emial.endswith("gmail.com"))
print("-"*44)
# Is the file CSV?
doc = "data_users.csv"
print(doc)
print("Is the file CSV:", doc.endswith(".csv"))
print("-"*44)
# 'substring' in 'string' --> checks if a word exists in the string
# Is this a valid email? "@"
emial = "diaz360arteaga@gmail.com"
print(emial)
print("Is this a valid email?:", "@" in emial)
print("-"*44)
# find() is great when combined with other methods to add dynamics
# find(substring) --> retuns the starting position of a word in the string
#Extract only phone numbres without country code
phone1 = "+52-176-12345"
phone2 = "52-654-16548"

print(phone1[phone1.find("-")+1:])
print(phone2[phone2.find("-")+1:])