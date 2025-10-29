"""
Number 1: True/False Tables
"""
#On my test I legit didn't know what this meant so i just said the one with the most, so if it was 2 falses or more I said false and two or more trues I said true
#To test it, I'm gonna make a funtoin to input the values and see what te result should be
"""
def true_false_tables():
    a = input("Enter true or false:")
    b = input("Enter true or false:")
    c = input("Enter true or false:")
    result = a && ( b ||c)
    print("The result is:", result)
    return result

true_false_tables()
"""
def truth(a, b, c):
   if (a and (b or c)):
       return True
   else:
       return False

#1
print(truth (False, False, False))
#2
print(truth (False, False, True))
#3
print(truth (False, True, False))
#4
print(truth (False, True, True))
#5
print(truth (True, False, False))
#6
print(truth (True, False, True))
#7
print(truth (True, True, False))
#8
print(truth (True, True, True))

"""
Number 2: Circle Area
"""
#I didn't know how to do this without the input, but it obviously can just be called, so idk why I was being stupid
a
import math
from math import pi
def circle_area(radius):
    area = math.pi * radius**2
    return area

circle_area(4)

"""
Number 3: Passwords    
"""
def passwords(password):
    for i in range 3:
        attempt = input("Enter your password:")
        if attempt == password:
            print("You have successfully logged in.")
            return passwords
        else:
            print("You're wrong, try again bruh.")
    print("You have been denied access.")
    return passwords

passwords("socialsecuritynumber")
