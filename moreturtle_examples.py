import turtle

#Screen is a complex data type-
#meaning it has attributes and behaviors
screen=turtle.Screen() #this is the instantiation call for the object screen
screen.title("Turtle Example in Python")

# Create a turtle object
# Turtle is a complex data type
poly=turtle.Turtle() #this is the instantiation of an object
poly.color("green")
poly.shape("classic")

# Move the turtle forward by 100 units
#---forward(100) is a nonfruitful function because it does not return a value, 
# it simply performs an action,
# which is to turn the turtle 90 degrees to the right
def forward100():
    poly.forward(100)

# Turn the turtle to the right by 90 degrees
#---right(90) is a nonfruitful function because
# it does not return a value
#it simply performs an action,
# which is to turn the turtle 90 degrees to the right
def right90():
    poly.right(90)

# Turn the turtle to the left by 90 degrees
#---left(90) is a nonfruitful function because
# it does not return a value
#it simply performs an action,
# which is to turn the turtle 90 degrees to the left
def left90():
    poly.left(90)

#subjects is a list which is a complex data type
#subjects contains a length of 5.
#for loop is for finite loops
#ITERATION - looping through code over and pver again
subjects = ["Math", "Science", "History", "Art", "PE"]
for subject in subjects:
    print("My favorite subject is ", subject)
    
counter=0
while(counter<= len(subjects)):
    print("Counter:", counter)
    #increment the counter
    counter=counter+1
    
def rainbow():
    colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
    for color in colors:
       poly.forward(10)
       poly.circle
       poly.forward(10)
       
poly.color("rainbow")

def backForth():
    poly.forward(-300)
    poly.speed(10)
    colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
    for color in colors:
        poly.color(color)
        poly.forward(100)
        poly.pensize(3)
        poly.forward(-50)

def funActivityWithTurtle():
    size=20
    #penup and pendown function
    
    #stamp function
    for i in range(30):
        poly.stamp()
        size=size+3
        poly.forward(size)
        poly.right(24)
        
funActivityWithTurtle()

#screen is a Screen object and it has behaviors
# Repeat the above steps to complete the square
for _ in range(3):
    screen.onkey(forward100, "Up")
    screen.onkey(right90, "Right")
    screen.onkey(left90, "Left")

screen.listen()
screen.mainloop()
# Keep the window open until clicked
turtle.done()
#do {
    #this code will run at least once
    #} while a condition is met
    

   