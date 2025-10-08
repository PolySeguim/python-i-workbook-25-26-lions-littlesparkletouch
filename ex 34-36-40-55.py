"""
Exercise 34:  Even or Odd?
Write a program that reads an integer from the user.  
Then your program should display a message indicating whether
the integer is even or odd    
"""
def Even_Odd():
    numberEntered = input("Enter an integer:")
    if int(numberEntered) % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")

#Even_Odd()
"""
Exercise 36:  Vowel or consonant
In this exercise you will create a program that reads a letter
of the alphabet from the user.  If the user enters a, e, i, o, or u
then your program should display a message indicating that the 
entered letter is a vowel.  If the user enters y then your program
should display a message indicating that sometimes y is a vowel, and 
sometimes y is a consonant.  Otherwise your program should display
a message indicating that the letter is a consonant.
"""
def Vowel_Consonant():
    letter = input("Enter a letter:")
    if letter in 'aeiouAEIOU':
        print("The letter is a vowel")
    elif letter in 'yY':
        print("Sometimes vowel, and sometimes consonant")
    else:
        print("The letter is consonant")
    

#Vowel_Consonant()
"""
Exercise 40:  Name that triangle
A triangle can be classified based on the lengths of its sides as
equilateral, isosceles, or scalene.  All 3 sides of an equilateral
triangle have the same length.  As isosceles triangle has two sides
that are the same length, and a third side that is a different length.
If all of the sides have different lengths then the triangle is scalene.

Write a program that reads the lengths of 3 sides of a triangle from the
user.  Display a message indicating the type of triangle

******  CHALLENGE:
Perform the same task as above but with angles and not sides.
"""
def Name_Triangle():
    tside1 = input("Enter length of 1 side of triangle:")
    tside2 = input("Enter length of 2 side of triangle:")
    tside3 = input("Enter length of 3 side of triangle:")
    if tside1 == tside2 == tside3:
            print("Equilateral triangle")
    elif tside1 == tside2 or tside2 == tside3 or tside1 == tside3:
            print("Isosceles triangle")
    else:
            print("Scalene triangle")    

#Name_Triangle()
"""
Exercise 55: Cell Phone Bill
A particular cell phone plan includes 50 minutes of air time and
50 text messages for $15.00 a month.  Each additional minute of 
air time costs $0.25 , while additional text messages cost $0.15
each.  All cell phone bills include an additional charge of $0.44
to support 911 call centers, and teh entire bill (including the 
911 charge) is subject to a 5 percent sales tax.

Write a program that reads the number of minutes and text messages
used in a month from the user.  Display the base charge, additional
minutes charge (if any), additional text message charge (if any), 
the 911 fee, tax and total bill amount.  Only display the additional 
minute and text charges if the user incurred costs in these 
categories.  Ensure that all of the charges are displayed using 2
decimal points
"""
def Phone_Bill():
    minutes = input("Enter number of minutes used:")
    texts = input("Enter number of text messages sent:")
    RegularPrice = 15.00
    if float(minutes) > 50:
        MinutesPrice = (float(minutes) - 50) * 0.25
    else:
        MinutesPrice = 0
    if float(texts) > 50:
        TextPrice = (float(texts) - 50) * 0.15
    else:
        TextPrice = 0
    Base = (RegularPrice + MinutesPrice + TextPrice)
    Tax = Base * 0.05
    Final = Base + Tax + 0.44
    print("Base charge: $", RegularPrice)
    if MinutesPrice > 0:
        print("Minutes charge: $", MinutesPrice)
    if TextPrice > 0:
        print("Text message charge: $", TextPrice)
    print("911 fee: $0.44")
    print("Tax: $", round(Tax, 2))
    print("Total bill: $" , round(Final, 2))
    
    Phone_Bill()