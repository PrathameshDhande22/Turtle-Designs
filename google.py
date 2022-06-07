# drawing google logo
from tkinter import Y
import turtle
def move(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()

t=turtle.Turtle()
turtle.title("Google Logo")
colors=["#4285F4","#DB4437","#F4B400","#0F9D58"]
""" #4285F4=blue colors 0
    #DB4437=red colors 1
    #F4B400=yellow colors 2 
    #0F9D58=green color 3  """
turtle.setup(width=900,height=650)
t.pensize(3)
t.speed(2)
#makes the blue color 
t.color(colors[0])
t.forward(150)
t.right(270)
t.circle(150,-60)

# print(f"Greeen Started x={t.xcor()} y={t.ycor()}")
# makes the greeen color
t.color(colors[3])
t.circle(150,-95)

# print(f"Yellow Started x={t.xcor()} y={t.ycor()}")
# makes the yellow color
t.color(colors[2])
t.circle(150,-45)
frx=t.xcor() # get the value for fill red x coordinate
fry=t.ycor()  # get the value for fill red y coordinate

# makes the red color
t.begin_fill()
t.fillcolor("red")
t.color(colors[1])
t.circle(150,-105)
# filling the colors in red
t.left(80)
t.forward(50)
t.left(95)
t.circle(-88,-120)
fyx=t.xcor() # get the value for fill yellow x coordinate
fyy=t.ycor()  # get the value for fill yellow y coordinate
t.setpos(frx,fry)
t.end_fill()

# fills the yellow colors
t.begin_fill()
t.fillcolor("#F4B400")
t.color(colors[2])
t.setposition(fyx,fyy)
t.circle(-140,-28)
# print(f"Yellow Started x={t.xcor()} y={t.ycor()}")
t.setpos(x=-135.9461680554974,y=-63.39273926110502)
t.left(6)
t.circle(-150,45)
t.end_fill()


# filling the green color
move(x=-135.9461680554974,y=-63.39273926110502)
t.right(10)
t.begin_fill()
t.fillcolor(colors[3])
t.color(colors[3])
t.setpos(x=-87.82209238377257,y=-32.18652786162181)
t.right(125)
t.circle(100,95)
# print(f"Greeen Started x={t.xcor()} y={t.ycor()}")
t.setpos(x=75.00000000000006,y=-129.9038105676658)
t.circle(150,-95)
t.end_fill()


# filling blue color
move(x=75.00000000000006,y=-129.9038105676658)
t.color(colors[0])
t.begin_fill()
t.fillcolor(colors[0])
t.setpos(x=52.013415405121336,y=-78.97483426798127)
t.left(90)
t.circle(70,43)
t.left(113)
t.forward(80+5+2)
t.home()
t.forward(150)
t.right(270)
t.circle(150,-60)
t.end_fill()
turtle.mainloop()