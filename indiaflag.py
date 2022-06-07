import turtle
t=turtle.Turtle()
turtle.setup(1000,600)
turtle.title("India Flag")
t.speed(3)

""" 
India flag made by Prathamesh Dhande on 11/02/2022 at 4:26 PM """

# this fuction moves the turtle to the passed arguements when it is called
def move(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

# Making Ashok chakra
t.color("blue")
t.pensize(4)
for i in range(24):
    t.forward(80)    
    t.backward(80)
    t.left(15)
move(0,-80)
t.circle(80)


# making the green color means the lower part of the flag
move(0,-90)
t.color("green")
t.begin_fill()
t.fillcolor("green")
t.forward(400)
t.backward(800)
t.right(90)
t.forward(180)
t.right(270)
t.forward(800)
t.right(270)
t.forward(180)
t.end_fill()

# making the upper part of the flag means saffron colour to the flag
move(-400,90)
t.color("orange")
t.begin_fill()
t.fillcolor("orange")
t.forward(180)
t.right(90)
t.forward(800)
t.right(90)
t.forward(180)
t.right(90)
t.forward(800)
t.end_fill()


t.hideturtle()
turtle.mainloop()