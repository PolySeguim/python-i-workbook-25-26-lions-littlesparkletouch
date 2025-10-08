import turtle

# screen is an object of the Screen class
screen = turtle.Screen()
screen.title("Clock Turtle")
screen.bgcolor("lightgreen")

#victoria is the object of the turtle class
victoria = turtle.Turtle()
victoria.shape("turtle")
victoria.color("blue")


def draw_clock():
    t.stamp()
    #loop variable
    #meaning that the i will be 1,2,3,4,5,6,7,8,9,10,11,12
    for i in range(12):
        t.stamp()
        t.penup()
        t.forward(150)
        t.pendown()
        t.stamp()
        t.penup()
        t.forward(-150)
        t.right(30)
        #victoria.stamp()
        #victoria.penup()
        #victoria.forward(150)
        #victoria.pendown()
        #victoria.stamp()
        #victoria.up(150)
draw_clock()
#t is an instanteoution of the turtle class
#sz is an integer datatype to determine the size of your square 
def draw_multicolor_square(t, sz, colors, thickness):
    t.pensize(thickness())
    for i in colors:
        t.color(i)
        t.forward(sz)
        t.left(90)

#draw_multicolor_square()
"""
#TEST SUITE
def test():
    test_turtle = turtle.Turtle()
    test_turtle.color("hotpink")
    #draw_square(test, tu)
    draw_clock #without a parameter
    screen_clock(t) #with turtle parameter
"""

def draw_square():
    for i in range(4):
       victoria.forward(100)
       victoria.right(90)
       victoria.forward(150)
       victoria.right(90)
       victoria.forward(200)     
       victoria.right(90)
       victoria.forward(250)
       victoria.right(90)
       victoria.forward(300)
       victoria.right(90)
       victoria.forward(350)
       victoria.right(90)
       victoria.forward(400)
       victoria.right(90)
       victoria.forward(450)   
#draw_square()

        
screen.listen()
screen.mainloop()
