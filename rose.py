import turtle

t=turtle.Turtle()
t.speed(2)
turtle.title("Rose")

t.penup()
t.goto(-50,250)
t.pendown()
t.color("black")
t.pensize(2)
name=turtle.textinput("Name","Enter Your Name")
try:
    t.write(name+" This Rose is for You",True,"right",["times new roman",15])
except:
    t.write("This Rose is for You",True,"right",["times new roman",15])
# making the rose 
t.penup()
t.goto(0,160)
t.pendown()
t.fillcolor("red")
t.begin_fill()
t.circle(10,180)
t.circle(25,110)
for i in range(20):
    t.left(3)
    t.forward(1)
for i in range(20):
    t.left(2)
    t.forward(2)
t.circle(30,120)
t.circle(50,130)
t.right(150)
t.forward(15)
t.left(110)
for i in range(50):
    t.left(1)
    t.forward(2)
t.circle(50,30)
t.home()
t.circle(80,110)
for i in range(83):
    t.forward(1)
t.circle(20,70)
for i in range(8):
    t.forward(1)
t.end_fill()


# making the stem of the rose
t.penup()
t.home()
t.pendown()
t.color("dark green")
t.pensize(6)
t.right(90)
for i in range(80):
    t.left(1)
    t.forward(3)
print(t.position())

# making the leaves
t.penup()
t.goto(23.78,-85.74)
t.pendown()
t.left(120)
t.pensize(2)
t.begin_fill()
t.fillcolor("light green")
for i in range(43):
    t.right(3)
    t.forward(2)
t.penup()
t.goto(23.78,-85.74)
t.pendown()
t.right(10)
for i in range(48):
    t.left(3)
    t.forward(2)
t.end_fill()

t.hideturtle()
turtle.mainloop()