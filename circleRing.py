import turtle
t=turtle.Turtle()
turtle.title("Circle Ring")
colors=["red","green","blue","yellow","orange","violet","purple"]
turtle.bgcolor("black")
t.speed(0)
for i in range(200):
    t.color(colors[i%7])
    t.pensize(i/11)
    t.forward(i)
    t.left(59)

turtle.mainloop()