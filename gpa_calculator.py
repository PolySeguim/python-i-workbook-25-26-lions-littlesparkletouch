"""
Exercise 51: Letter Grade to Grade Points
At a particular university, letter grades are mapped to grade
points in the following manner:
Letter Grade points
A+ 4.0
A 4.0
A- 3.7
B+ 3.3
B 3.0
B- 2.7
C+ 2.3
C 2.0
C- 1.7
D+ 1.3
D 1.0
F 0
Write a program that begins by reading a letter grade from the
user. Then your program should compute and display the equivalent
number of grade points. Ensure that your program generates an
appropriate error message if the user enters an invalid letter
grade.
"""

A_PLUS= 4.0
A= 4.0
A_MINUS= 3.7
B_PLUS= 3.3
B= 3.0
B_MINUS= 2.7
C_PLUS= 2.3
C= 2.0
C_MINUS= 1.7
D_PLUS= 1.3
D= 1.0
F= 0
INVALD = -1

def letterToGPA():
    letter = input("Enter a letter grade:")
    if(letter == "A+" or letter == "A"):
        gpa = 4.0
    elif(letter == "A-"):
        gpa = 3.7
    elif(letter == "B+"):
        gpa = 3.3
    elif(letter == "B"):
        gpa = 3.0
    elif(letter == "B-"):
        gpa = 2.7
    elif(letter == "C+"):
        gpa = 2.3
    elif(letter == "C"):
        gpa = 2.0
    elif(letter == "C-"):
        gpa = 1.7
    elif(letter == "D+"):
        gpa = 1.3
    elif(letter == "D"):
        gpa = 1.0
    elif(letter == "F"):
        gpa = 0
    else:
        gpa = -1
    print(gpa)
    
#letterToGPA()
    
"""

def readLetter():
    letter = input("Enter a letter grade:")
    return letter

readLetter()

def assignGPA():
    gpa = 0
    if(letter == "A+" or letter == "A"):
        gpa = A
    elif(letter == "A-"):
        gpa = A_MINUS
    elif(letter == "B+"):
        gpa = B_PLUS
    elif(letter == "B"):
        gpa = B
    elif(letter == "B-"):
        gpa = B_MINUS
    elif(letter == "C+"):
        gpa = C_PLUS
    elif(letter == "C"):
        gpa = C
    elif(letter == "C-"):
        gpa = C_MINUS
    elif(letter == "D+"):
        gpa = D_PLUS
    elif(letter == "D"):
        gpa = D
    elif(letter == "F"):
        gpa = F
    else:
        gpa = INVALD
    
    print(gpa)
    return gpa

assignGPA()

def getGPA():
    givenGPA = float(input("Enter a GPA:"))
    return givenGPA

getGPA()

"""

"""
Exercise 52: In the previous exercises you created a program that
converts a letter grade into the equivalent number of grade points.
In this exercise you will create a program that reverses the process
and converts from a grade point value entered by the user to a letter
grade. Ensure that your program handles grade point values that fall
between letter grades. These should be rounded to the closes letter
grade. Your program should report A+ for a 4.0 (or greater) grade
point average.
"""
def gpaToLetter():
    insertGPA = float(input("Enter a GPA:"))
    if(insertGPA >= 4.0):
        letterGrade = "A+"
    elif(insertGPA >= 3.7):
        letterGrade = "A-"
    elif(insertGPA >= 3.3):
        letterGrade = "B+"
    elif(insertGPA >= 3.0):
        letterGrade = "B"
    elif(insertGPA >= 2.7):
        letterGrade = "B-"
    elif(insertGPA >= 2.3):
        letterGrade = "C+"
    elif(insertGPA >= 2.0):
        letterGrade = "C"
    elif(insertGPA >= 1.7):
        letterGrade = "C-"
    elif(insertGPA >= 1.3):
        letterGrade = "D+"
    elif(insertGPA >= 1.0):
        letterGrade = "D"
    else:
        letterGrade = "F"
    print(letterGrade)
    
#gpaToLetter()
"""
Exercise 66: Compute a Grade Point Average
Exercise 51 includes a table that shows the conversion from letter
grades to grade points at a particular academic institution. In this
exercise you will compute the grade point average of an arbitrary number
of letter grades entered by teh user. The user will enter a blank
line to indicate that all of the grades have been provided. For example,
if the user enters A, followed by C+, followed by B, followed by a blank
line then your program should report a grade point average of 3.1.
You may find your solutions to Exercise 51 helpful when completing this
exercise. Your program does not need to do any error checking. It can
assume that each value entered by the user will be a valid letter grade
or a blank line.
"""
def computeGPA():
    totalPoints = 0
    count = 0
    while True:
        letter = input("Enter a letter grade:")
        if letter == "":
            break
        if(letter == "A+" or letter == "A"):
            gpa = A
        elif(letter == "A-"):
            gpa = A_MINUS
        elif(letter == "B+"):
            gpa = B_PLUS
        elif(letter == "B"):
            gpa = B
        elif(letter == "B-"):
            gpa = B_MINUS
        elif(letter == "C+"):
            gpa = C_PLUS
        elif(letter == "C"):
            gpa = C
        elif(letter == "C-"):
            gpa = C_MINUS
        elif(letter == "D+"):
            gpa = D_PLUS
        elif(letter == "D"):
            gpa = D
        elif(letter == "F"):
            gpa = F
        
        totalPoints += gpa
        count += 1
    
    if count > 0:
        averageGPA = totalPoints / count
        print("Grade Point Average:", averageGPA)
    else:
        print("No grades were entered.")
        
#computeGPA()