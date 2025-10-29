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
#Now i realize it yay!
import math
from math import pi
def circle_area(radius):
    area = math.pi * radius**2
    return area

circle_area(4)

"""
Number 3: Passwords    
"""
#I didn't even realize i was a thing I could use, but now I understand it yay!
def passwords(password):
    for i in range 3:
        attempt = input("Enter your password:")
        if attempt == password:
            print("You have successfully logged in.")
            return passwords
        else:
            print("You're wrong, try again.")
    print("You have been denied access.")
    return passwords

passwords("socialsecuritynumber")

"""
Number 4: a boolean is an expression that is either true or false
"""
"""
Number 5: 
== is equal to in a comparison
!= is not equal to
> is greater than
< is less than
>= is greater than or equal to
<= is less than or equal to
"""
"""
Number 6: What will the code print
"""
#I didn't even know what the code was
#I guessed and idk how to make it run so i still don't know what it does
def test():
    for i in [12, 16, 17 24, 29]:
        if i % 2 == 1:
            break
        print(i)
    print("done")

test()

"""
Number 7: What will it print again
"""
#Again I didn't know what the code was
def test2():
    for i in [12, 16, 17, 24, 29]:
        if i % 2 == 1:
            continue
        print(i)
    print("done")
    
"""
Number 8: Code
"""
#I'm guessing I was right since there's the red squiggly lines under tha print, so it can't print so bang.
def test3():
    x=5
    if x==5:
        print "Wow, X is EXACTLY five!"
    elif x>5:
        print "X is now MORE than five!"
    else:
        print "X is now LESS than five!"
        
test3()

"""
Number 9: Code again
"""
#I guessed it was a turtle that made a square.
def functionA(T, side, num):
    for i in range(num):
        square(t, side)
        t.penup()
        t.forward(side*2)
        t.pendown()

functionA(t, 20, 4)

"""
Number 10: Code again.
"""
#I said it would just move forward and right, but I now know what i in range means, so its gonna make a pentagon because it has 5 sides.
def functionB():
    for i in range(5):
        t.forward(100)
        t.right(72)

functionB()