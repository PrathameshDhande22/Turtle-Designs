import turtle

t = turtle.Turtle()


def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()


def test(x, y, f):
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.forward(f)
    print(f"x={t.xcor()} & y={t.ycor()}")
    t.hideturtle()

turtle.setup(1300, 700)
t.speed(3)

# printing PRATHAMESH
# making P
move(-600, 0)
t.pensize(8)
t.pencolor("red")
t.left(90)
t.forward(150)
t.right(90)
move(-600, 70)
t.circle(40, 180)
t.right(90)

# making R
move(-530, 0)
t.color("green")
t.forward(150)
move(-530, 70)
t.right(90)
t.circle(40, 180)
move(-530, 70)
t.right(240)
t.forward(80.62)


# making A
move(-460, 0)
t.color("blue")
t.left(140)
t.forward(150)
t.right(155)
t.forward(152.8322890084709513)
t.left(74)
move(-450.00152304843607,69.82547593562717)
t.forward(36)

# making T
t.color("orange")
t.left(2)
move(-395,145)
t.forward(100)
t.backward(50)
t.right(90)
t.forward(145)

# making H
t.color("aqua")
move(-275,0)
t.left(180)
t.forward(150)
t.back(75)
t.right(90)
t.forward(50)
t.left(90)
t.forward(75)
t.back(150)

# making A
move(-206, 0)
t.color("blue")
t.right(13)
t.forward(150)
t.right(155)
t.forward(152.8322890084709513)
t.left(75)
move(-196.01370465245427,69.47664043757057)
t.forward(38)

# making m
move(-120,0)
t.color("violet")
t.left(93)
t.forward(150)
t.right(140)
t.forward(90)
t.left(105)
t.forward(90)
t.right(143)
t.goto(-13.245187044079586,0)

# making E
move(7,0)
t.color("grey")
t.left(177)
t.forward(150)
t.right(90)
t.forward(75)
move(7,75)
t.forward(46)
move(7,0)
t.forward(75)

# making S
t.color("black")
move(118,75)
t.circle(37.5)
t.color("white")
t.circle(37.5,160)
move(118,0)
t.color("black")
t.right(180-20)
t.forward(5)
t.circle(37.5,188)

# making H
t.color("aqua")
move(175,0)
t.right(98)
t.forward(150)
t.back(75)
t.right(90)
t.forward(50)
t.left(90)
t.forward(75)
t.back(150)
t.hideturtle()





turtle.mainloop()
