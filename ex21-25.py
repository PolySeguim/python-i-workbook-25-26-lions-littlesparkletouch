import math
from math import pi
from math import tan
from math import radians

"""
Exercise 21: Area of a Triangle
The area of a triangle can be computed using the following formula,
where b is the length of the base of the triangle, and h is its
height:
area = (b*h)/2
Write a program that allows the user to enter values for b and h.
The program should then compute and display the area of a triangle
with base length b and height h
"""
def Area_Triangle():
    b = input("Enter the length of the base of the triangle:")
    h = input("Enter the height of the triangle:")
    areaTriangle = (float(b) * float(h)) / 2
    print("Area of the triangle:" , areaTriangle)
    
#Area_Triangle()
"""
Exercise 22: Area of a triangle (Again)
In the previous exercise you created a program that computed the area
of a triangle when the length of its base and its height were known.
It is also possible to compute the area of a triangle when the lengths
of all three sides are known. Let s1, s2, and s3 be the lengths of the
sides. Let s = (s1 + s2 + s3)/2. Then the area of a triangle can be
calculated using the following formula:
area = (s * (s - s1) * (s - s2) * (s - s3))**(1/2)
Develop a program that reads the lengths of the sides of a triangle from
the user and display its area.
"""
def Area_Triangle_Again():
    s1 = input("Enter length of side 1:")
    s2 = input("Enter length of side 2:")
    s3 = input("Enter length of side 3:")
    s = (float(s1) + float(s2) + float(s3)) / 2
    AreaTriangleAgain = (s * (s - float(s1)) * (s - float(s2)) * (s - float(s3)))**(1/2)
    print("Area of the triangle:" , AreaTriangleAgain)

#Area_Triangle_Again()
"""
Exercise 23: Area of a Regular Polygon
A polygon is regular if its sides are all the same length and the angles
between all of the adjacent sides are equal. The area of a regular polygon
can be computed using the following formula, where s is the length of a side
and n is the number of sides:
area = (n * s**(2))/(4 * tan(pi/n))
Write a program that reads s and n from the user and then displays the area
of a regular polygon constructed from these values.
"""
def Area_Regular_Polygon():
    s = input("Enter the length of a side:")
    n = input("Enter the number of sides:")
    AreaRegPolygon = (int(n) * float(s)**(2)) / (4 * tan(pi/int(n)))
    print("Area:" , AreaRegPolygon)

#Area_Regular_Polygon()
"""
Exercise 24: Units of Time
Create a program that reads a duration from the user as a number of days,
hours, minutes, and seconds. Compute the total number of seconds represented
by this duration.
"""
def Units_of_Time():
    days = input("Enter days:")
    hours = input("Enter hours:")
    minutes = input("Enter minutes:")
    seconds = input("Enter seconds:")
    TotalSeconds = (float(days) * 86400) + (float(hours) *  3600) + (float(minutes) * 60) + float(seconds)
    print("Total seconds:" , TotalSeconds)

#Units_of_Time()
"""
Exercise 25: Units of Time (again)
In this exercise you will reverse the process described in the previous
exercise. Develop a program that begins by reading a number of seconds from
the user. Then your program should display the equivalent amount of time
in the form D:HH:MM:SS, where D, HH, MM, and SS represent days, hours,
minutes and seconds respectively. The hours, minutes and seconds should all
be formatted so that they occupy exactly two digits, with a leading 0 displayed
if necessary.
"""
def Units_Time_Again():
    TotSeconds = input("Enter total seconds:")
    daysAgain = int(float(TotSeconds) // 86400)
    hoursAgain = int(float(TotSeconds) % 86400) // 3600
    minutesAgain = int(((float(TotSeconds) % 86400) % 3600) // 60)
    secondsAgain = int(((float(TotSeconds) % 86400) % 3600) % 60)
    print("D:HH:MM:SS is" , daysAgain , ":" , hoursAgain , ":" , minutesAgain , ":" , secondsAgain)
    
#Units_Time_Again()

