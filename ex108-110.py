"""
Exercise 108: Negatives, Zeros, and Positives
Create a program that reads integers from the user until a blank
line is entered. Once all of the integers have been read your
program should display all the negative numbers, followed by all
of the zeros, followed b y all of the positive numbers. Within each
group the numbers should be displayed in the same order that they were
entered by the user. For example, if the user enters the values
3, -4, 1, 0, -1, 0, and -2 then your program should output the values
-4, -1, -2, 0 ,0 , 3, and 1. Your program should display each value
on its own line.
"""

integers = []
def readInteger():

    
    user_input = input("Enter an integer:")
    while user_input != "":
        userInput = int(user_input)
        integers.append(userInput)
        user_input = input("Enter an integer:")
    return integers

readInteger()

def displayIntegers():
    negatives = []
    zeros = []
    positives = []
    for number in integers:
        if number < 0:
            negatives.append(number)
        elif number == 0:
            zeros.append(number)
        else:
            positives.append(number)
    return negatives, zeros, positives

print(displayIntegers())

"""
def displayIntegers():
    negatives = []
    zeros = []
    positives = []
    
    for number in readInteger():
        if number < 0:
            negatives.append(number)
        elif number == 0:
            zeros.append(number)
        else:
            positives.append(number)
    
    for number in negatives + zeros + positives:
        print(number)
        
displayIntegers()
"""
"""
def in_Order():
    integers = readInteger()
    negatives = [num for num in integers if num < 0]
    zeros = [num for num in integers if num == 0]
    positives = [num for num in integers if num > 0]
    
    return negatives , zeros , positives
    

in_Order()

"""

"""
Exercise 109: List of Proper Divisors
A proper divisor of a positive integer, n, is a positive integer
less than n which divides evenly into n. Write a function that
computes all of the proper divisors of a positive integer. The
integer will be passed to the function as its only parameter.
The function will return a list containing all of the proper divisors
as its only result. Complete this exercise by writing a main program
that demonstrates the function by reading a value from the user and
displaying the list of its proper divisors. Ensure that your main
program only runs when your solution has not been imported into
another file
"""
def 
"""
Exercise 110: Perfect Numbers
An integer, n, is said to be perfect when the sum of all the proper
divisors of n is equal to n. For example, 28 is a perfect number
because its proper divisors are 1, 2, 4, 7, and 14, and 1+2+4+7+14 = 28.
Write a function that determines whether or not a positive integer is
perfect. Your function will take one parameter. If that parameter is a
perfect number then your function will return true. Otherwise it will
return false. In addition, write a main program that uses your
function to identify and display all of the perfect numbers between 1 and
10,000. Import your solution to Exercise 109 when completing this task.
"""
