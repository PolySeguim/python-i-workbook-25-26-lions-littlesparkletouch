import math
from math import log10, sin, cos, acos
"""
Exercise 6: Tax and Tip
The program you create for this exercise will begin by reading the cost
of a meal ordered at a restaurant from the user.  Then your program will
compute the tax and tip for the meal.  Use your local tax rate when 
computing the amount of tax owing.  Compute the tip as 18 percent of  the 
meal amount (without tax).  The output from your program should include
both the tax and the tip.  Format the output so that all of the values
are displayed using two decimal places.  (17 lines)
"""
meal=input("Cost of meal:")
NoTaxWithTip = float(meal) * 0.18 + float(meal)
WithTaxAndTip = float(NoTaxWithTip) + float(meal) * 0.078
refund=round(WithTaxAndTip, 2)
print("Final cost:" , float(WithTaxAndTip))
"""
Exercise 7:  Sum of the First n Positive Integers
Write a program that reads a positive integer, n, from the user and 
then displays the sum of all the integers from 1 to n.  The sum of the 
first n positive integers can be computed using the formula:
sum = (n*(n+1))/2
(12 lines)
"""
integer=input("positive integer:")
Sum=(int(integer) * (int(integer) + 1) / 2)
print(Sum)
"""
Exercise 8:  Widgets and Gizmos
An online retailer sells two products:   widgets and gizmos.  Each widget 
weighs 75 grams.  Each gizmo weighs 112 grams.  Write a program that reads
the number of gizmos in an order from the user.  Then your program should 
compute and display the total weight of the order.  (15 lines)

"""
gizmos=input("Enter number of gizmos:")
weightGizmos=(float(gizmos) * 112)
print(weightGizmos , "grams")
"""
Exercise 9:  Compound Interest
Pretend that you have just opened a new savings account that earns 4 percent
interest per year.  The interest that you earn is paid at the end of the year, 
and is added to the balance of the savings account.  Write a program that begins
by reading the amount of money deposited into the account from the user.  Then 
your program should compute and display the amount in the savings account after
1, 2, and 3 years.  Display each amount so that it is rounded to 2 decimal 
places.  (19 lines)
"""
OrigAmount=input("Amount deposited:")
OneYearAmount= (float(OrigAmount) * 1.04)
TwoYearAmount=(float(OneYearAmount) * 1.04)
ThreeYearAmount=(float(TwoYearAmount)* 1.04)
print("Amount after 1 year:" , OneYearAmount)
print("Amount after 2 years:" , TwoYearAmount)
print("Amount after 3 years:" , ThreeYearAmount)
"""
Exercise 10:  Arithmetic
Create a program that reads two integers, a and b, from the user.  Your program
should compute and display:
- the sum of a and b
- the difference when b is subtracted from a
- the product of a and b
- the quotient when a is divided by b
- the remainder when a is divided by b
- the result of log10 a
- the result of a to the power of b

Hint:  you will probably find the log10 function in the math module helpful
for computing the second last item in the list.
"""
a=input("Enter integer a:" )
b=input("Enter integer b:" )
sum=(int(a) + int(b))
print("Sum:" , sum)
difference=(int(b) - int(a))
print("Difference:" , difference)
product=(int(a) * int(b))
print("Product:" , product)
quotient=(int(a)/int(b))
print("Quotient:" , quotient)
remainder=(int(a)%int(b))
print("Remainder:" , remainder)
log=(log10(int(a)))
print("Log10:" , log)
power=(int(a)^int(b))
print("Power:" , power)
if __name__ == "__main__":
    print("Hi there!")