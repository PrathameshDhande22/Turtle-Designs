import turtle
t=turtle.Turtle()
s=turtle.Screen()
s.bgcolor("black")
t.pencolor("#ffb6c1")
c=[ "#ff75ba","#ff389c","#ff0f87","#e3256b","#bf1f5a"]
for i in range(150):
    for j in range(1):
        t.speed(0)
        t.pensize(2)
        t.circle(i*2,100)
    t.lt(120)
    t.pencolor(c[i%5])
turtle.mainloop()