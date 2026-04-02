# Indexex & Slicing
# 1-Indexing --> extracts one character by position  'string'[index]
text = "Python"
print("How many characters has " + text + ":", len(text))
print("-"*30)
# Extract the first character
print("Extract the first character:", text[0])
# or
print("Extract the first character:", text[-6])
#-------------
print("-"*30)
#-------------
# Extract the last character
print("Extract the last character:", text[5])
# or
print("Extract the last character:", text[-1])
#-------------
print("-"*30)
#-------------
# Extract the h character
print("Extract h:", text[3])
# or
print("Extract h:", text[-3])
#-------------
print("-"*30)
#-------------
# 2-Slicing --> extracts a part of the string
date = "2026-09-20"
print("How many characters has " + date + ":", len(date))
#-------------
print("-"*30)
#-------------
# Extract the year "2026"
print("Extract the year:", date[0:4])
# or
print("Extract the year:", date[-10:-6])
#or
print("Extract the year:", date[:4])
#-------------
print("-"*30)
#-------------
# Extract the Month "09"
print("Extract the Month:", date[5:7])
# or
print("Extract the Month:", date[-5:-3])
#-------------
print("-"*30)
#-------------
# Extract the Day "20"
print("Extract the Day:", date[8:])
# or
print("Extract the Day:", date[-2:])