#all import statements at the top of the file
import math
"""
"""
#Functions are either void or fruitful
"""
#Global variablilty
f_name = ""

#FUNCTION DECLARATONS
#void function

#Void function
def setName(fname):
    f_name = fname
    print(fname)
    
#Function Calls
setName("Poly")
setName("Amanda")
setName("Tess")

#Function header: writing why
sum(list of numbers)
    #function <-- adds up a list of numbers

author: Poly (10/8/2025)

Returns:
_type_: _description_

name = getName()
print("Hi" , name)

def getName():

getName()
    
def sum(numbers):
    sum = 0
    for i in numbers::
    sum += i
        #print(sum)
    return sum

sum()

def absoluteValue(x):
    if x < 0:
        return -x #the return statement exits the function
    else:
        return x
    
absoluteValue(-8)

    
def distance(x1, y1, x2, y2):
    dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    #return (((x2 - x1)**2) + ((y2 - y1)**2))**0.5
    
#Boolean functions return a true or false value

def isDivisible(x, y):
    if (x % y == 0):
        return True
    else:
        return False


#Function Calls

    #num = 1,2,3,4,5,6,7,8,9,10,10
    num1 = 2.3, 4.2, 6.2, 7.3
    test1 = sum(num1)
    print(test1)
    

num1 = 1,2,3,4,5
print(absVal(-23))

print(distance(1,2,3,4))
"""
"""
"""
  
#A fruitful function that compares integers and ***returns the largest integers
def maxInt(a, b):
    if a > b:
        return a
    elif a == b:
        return "The numbers are equal"
    else:
        return b       

maxInt(15, 10)


#A fruitul hypotenuse function that ***returns the calue of the hypotenuse given the a and b values 

def hypotenuse(a, b):
    c = math.sqrt(a**2 + b**2)
    return c
#hypotenuse(3,4)

#A fruitful sloipe function that returns the slope of a line given 4 parametersn (x1, x2, y1, y2)


#A fruitful intercept function that returns the y-intercept given the two points (x1, x2, y1, y2)
#****This function should call the slope function in order to calculate the y-intercept or b-value


#A fruitful fucntion that will calculate whether a numver is a factor of another number
#**returns a BOOLEAN (returns true or false)
#*** Is 3 a factor of 9?


#A fruitful fucntion that will calculate whether a numver is a factor of another number
#***is 12 a facror of 9
#***return a boolean (true or false)