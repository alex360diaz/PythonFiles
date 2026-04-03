# Pyhon Challenge
# Create 5 variables - each with a different data type:
# 1- Age
# 2- Height (with decimals)
# 3- Name
# 4- Are you a student?
# 5- Something with no value yet
# Create 5 variables - each with a different data type:
# 1. Your age
# 2. Your height (with decimals)
# 3. Your name
# 4. Are you a student?
# 5. Somethin with no vlaue yet
# Them print the values, data types, lenghs of all data vaiables

age = int(input("Type your age: "))
height = float(input("Type your height with decimals: "))
name = input("Type your name: ")
student_status = bool(input("Are you a student (True or False): "))
x = None

print("Age: ",age,
      "\nHeight: ",height,
      "\nName: ",name,
      "\nStudent: ",student_status,
      "\nx: ",x )
print("\n--------------------")
print("Age:",type(age))
print("Height:",type(height))
print("Name:",type(name))
print("Student status:",type(student_status))
print("x:",type(x))
print("----------------------\n")

print("Lengths of all variables")
print("Age :",age.bit_length())
print("Name :",len(name))
