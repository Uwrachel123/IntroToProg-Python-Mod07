#--------------------------------------
# Title: Assignment 7
# Description: Handling Exception and Pickling
# Foundation of Programming, Python
# Rachel M Woo, 5.22-23.2021,Created Script
#---------------------------------------
# Data ---------------------------------
FileName = 'PickleFile.dat'
objFile = None 
strTask = ''
strPriority = ''
lstUserInput = ''

#---------------------------------------

# Handling Exception - handle a single exception
try:
 Value = int(input("Type a number between 1 and 100: "))
except ValueError: print("You must type a number between 1 and 100!")
else:
 if (Value > 0) and (Value <= 100): print("You typed: ", Value)
 else: print("The value you typed is incorrect!")

# Handling Exception - specific exception, reciprocal of even numbers

try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0
except:
    print("Not an even number!")
else:
     reciprocal = 1/num
     print(reciprocal)

# Handling Exception - Raising exception
try:
    a = int(input("Enter a positive integer: "))
    if a <= 0:
      raise ValueError("That is not a positive number!")
except ValueError as ve:
    print(ve)

# Pickling - storing data in a binary file

import pickle

strTask = str(input("Enter your task: "))
strPriority = str(input("Enter your priority: "))
lstUserInput = [strTask, strPriority]
print(lstUserInput)

objFile = open("PickleFile.dat", "ab")
pickle.dump(lstUserInput, objFile)
objFile.close()

objFile = open("PickleFile.dat", "rb")
objFileData = pickle.load(objFile)
objFile.close()

print(objFileData)

