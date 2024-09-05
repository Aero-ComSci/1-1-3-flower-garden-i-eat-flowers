import turtle as t
import random
painter = t.Turtle()
#remember to parase the thingy to search for numbers inside of the input
numberset = set(range(1,101))
flowerlist = ["rose", "sunflower", "tulip", "chrysanthemum", "orchid"]

def randompos():
    x_min, x_max = -200, 200  # Example x boundaries
    y_min, y_max = -250, 250  # Example y boundaries
    x = random.uniform(x_min, x_max)
    y = random.uniform(y_min, y_max)
    painter.goto(x,y)

def rose():
    painter.pencolor("black")
# Set initial position
    painter.penup()
    painter.left(90)
    painter.fd(100)  # Half of 200
    painter.pendown()
    painter.right(90)

    # Flower base
    painter.fillcolor("red")
    painter.begin_fill()
    painter.circle(5, 180)  # Half of 10
    painter.circle(12.5, 110)  # Half of 25
    painter.left(50)
    painter.circle(30, 45)  # Half of 60
    painter.circle(10, 170)  # Half of 20
    painter.right(24)
    painter.fd(15)  # Half of 30
    painter.left(10)
    painter.circle(15, 110)  # Half of 30
    painter.fd(10)  # Half of 20
    painter.left(40)
    painter.circle(45, 70)  # Half of 90
    painter.circle(15, 150)  # Half of 30
    painter.right(30)
    painter.fd(7.5)  # Half of 15
    painter.circle(40, 90)  # Half of 80
    painter.left(15)
    painter.fd(22.5)  # Half of 45
    painter.right(165)
    painter.fd(10)  # Half of 20
    painter.left(155)
    painter.circle(75, 80)  # Half of 150
    painter.left(50)
    painter.circle(75, 90)  # Half of 150
    painter.end_fill()

    # Petal 1
    painter.left(150)
    painter.circle(-45, 70)  # Half of 90
    painter.left(20)
    painter.circle(37.5, 105)  # Half of 75
    painter.setheading(60)
    painter.circle(40, 98)  # Half of 80
    painter.circle(-45, 40)  # Half of 90

    # Petal 2
    painter.left(180)
    painter.circle(45, 40)  # Half of 90
    painter.circle(-40, 98)  # Half of 80
    painter.setheading(-83)

    # Leaves 1
    painter.fd(15)  # Half of 30
    painter.left(90)
    painter.fd(12.5)  # Half of 25
    painter.left(45)
    painter.fillcolor("green")
    painter.begin_fill()
    painter.circle(-40, 90)  # Half of 80
    painter.right(90)
    painter.circle(-40, 90)  # Half of 80
    painter.end_fill()
    painter.right(135)
    painter.fd(30)  # Half of 60
    painter.left(180)
    painter.fd(42.5)  # Half of 85
    painter.left(90)
    painter.fd(40)  # Half of 80

    # Leaves 2
    painter.right(90)
    painter.right(45)
    painter.fillcolor("green")
    painter.begin_fill()
    painter.circle(40, 90)  # Half of 80
    painter.left(90)
    painter.circle(40, 90)  # Half of 80
    painter.end_fill()
    painter.left(135)
    painter.fd(30)  # Half of 60
    painter.left(180)
    painter.fd(30)  # Half of 60
    painter.right(90)
    painter.circle(100, 60)  # Half of 200


def sunflower():
    painter.pencolor("yellow")
    painter.forward(10)
    painter.circle(50)
    painter.forward(10)
    painter.circle(50)

john = input('What do you want to draw?')
johnlower = john.lower()
johnsplit = johnlower.split()
flowerfound = False
numberfound = False
coolset = set(flowerlist)
for word in johnsplit:
    if word in coolset:
        flowerfound = True
        print("Yippiee")
        painter.speed(0)
        if word == "rose":
            randompos()
            rose()
            painter.penup()
        if word == "sunflower":
            randompos()
            sunflower()
            painter.penup()
        for number in coolset:
            if number in numberset:
                numberfound = True
                print("Yippiee")
                painter.speed(0)
                if word == "rose":
                    rose()
                if word == "sunflower":
                    sunflower()
if not flowerfound:
    print ("Donde esta la flora?")

t.done()
