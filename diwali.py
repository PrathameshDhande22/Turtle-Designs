import turtle
turtle.bgcolor("black")
turtle.title("Happy Diwali")
turtle.setup(1000,700,startx=200,starty=50)  
t=turtle.Turtle()

def move(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()



t.pensize(3)
t.turtlesize(2)

#making the 1st diya
move(-420,-200)
t.pensize(2)
t.pencolor('black')
t.begin_fill()
t.fillcolor("#fab578")
t.right(40)
t.circle(180,80)
t.left(100)
t.circle(180,80)
t.end_fill()
t.begin_fill()
t.fillcolor('brown')
t.left(50)
t.circle(117,180)
t.right(50)
t.circle(180,-80)
t.end_fill()
move(-185.99999999999983,-200.0)
t.left(70)
t.begin_fill()
t.fillcolor('yellow')
t.circle(70,120)
t.left(60)
t.circle(70,120)
t.end_fill()

# text happy diwali
move(-50,0)
t.color('#00e5ff')
t.write('HAPPY DIWALI',font=("Ink Free",50))


def crackers():
    for i in range(18):
        t.forward(80)
        t.back(80)
        t.left(20)
# crackers 
def crack_display():
    t.pensize(5)
    coord=[(-350,250),(-70,190),(190,220)]
    colors=['red','#3cff00','#fff700']
    for i in range(3):
        coordinates=coord[i]
        t.color(colors[i])
        move(coordinates[0],coordinates[1])
        crackers()

# lavangi phataka
t.color('black')
t.pensize(2)
move(-453,-27)
t.left(65)
t.begin_fill()
t.fillcolor('red')
t.forward(180)
t.circle(-15,180)
t.forward(180)
t.end_fill()
move(-455,-29)
t.begin_fill()
t.fillcolor('brown')
t.circle(15)
t.end_fill()
move(-287,74)
t.pencolor('grey')
t.left(180)
t.pensize(6)
t.forward(30)
t.circle(-60,70)
    

# lantern
move(363,25)
t.color('white')
t.pensize(2)
t.right(55)
t.fd(60)
t.right(90)
t.color('black')
t.begin_fill()
t.fillcolor('#ae00ff')
t.forward(50)
t.left(90)
t.forward(30)
t.left(90)
t.fd(100)
t.left(90)
t.fd(30)
t.left(90)
t.fd(50)
t.end_fill()
move(312,-65)

t.begin_fill()
t.fillcolor('#ff7700')
t.circle(40,180)
t.forward(100)
t.circle(40,180)
t.end_fill()
move(311,-145)

t.begin_fill()
t.fillcolor("#ae00ff")
t.left(90)
t.fd(30)

t.left(90)
t.fd(100)
t.left(90)
t.fd(30)
t.end_fill()
move(310,-175)
t.left(180)
t.color('#ff8c00')
t.pensize(7)
for i in range(5):
    t.forward(120)
    t.back(120)
    t.left(90)
    t.fd(20)
    t.right(90)
    if i==4:
        t.fd(120)


t.speed(0)
crack_display()




t.hideturtle()
turtle.done()

