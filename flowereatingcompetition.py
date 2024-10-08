import turtle as t
import random
import re 

painter = t.Turtle()
flowerlist = ["rose", "sunflower", "tulip", "chrysanthemum", "orchid"]
painter.speed(0)
def randompos():
    x_min, x_max = -200, 200
    y_min, y_max = -250, 250
    x = random.uniform(x_min, x_max)
    y = random.uniform(y_min, y_max)
    painter.penup()
    painter.goto(x, y)
    painter.pendown()

def rose():
    painter.pencolor("black")
    painter.fillcolor("red")
    painter.begin_fill()
    painter.circle(10)
    painter.end_fill()
    painter.pencolor("green")
    painter.setheading(0)
    painter.right(90)
    painter.forward(20)

def sunflower():
    painter.pencolor("yellow")
    painter.fillcolor("yellow")
    painter.begin_fill()
    for _ in range(12):
        painter.circle(50, 60)
        painter.left(120)
        painter.circle(50, 60)
        painter.left(120)
        painter.left(30)
    painter.end_fill()
    painter.pencolor("brown")
    painter.setheading(0)
    painter.penup()

def tulip():
    painter.pencolor("orange")
    painter.fillcolor("orange")
    painter.begin_fill()
    painter.setheading(-90)
    painter.circle(30, 180)
    painter.end_fill()
    painter.pencolor("green")
    painter.setheading(-90)
    painter.width(5)
    painter.forward(80) 
    painter.width(1)


def chrysanthemum():
    painter.pencolor("brown")
    painter.fillcolor("yellow")
    painter.begin_fill()
    for _ in range(18):
        painter.circle(30, 60)
        painter.right(120)
        painter.circle(30, 60)
        painter.right(120)
        painter.right(20)
    painter.end_fill()

def orchid():
    painter.pencolor("purple")
    painter.fillcolor("purple")
    painter.begin_fill()
    painter.circle(5)
    painter.end_fill()

    painter.setheading(0)
    painter.forward(10)  # Move to the start of the petals

    for _ in range(4):
        painter.fillcolor("purple")
        painter.begin_fill()
        painter.circle(15, 90)  # Draw one side of the petal
        painter.left(90)
        painter.circle(15, 90)  # Draw the other side of the petal
        painter.end_fill()
        painter.right(90)  # Reset heading
        painter.forward(10)  # Position for the next petal
        painter.left(90)  # Adjust heading for the next petal



def drawflowers(flower, quantity):
    for _ in range(quantity):
        randompos()
        if flower == "rose":
            rose()
        elif flower == "sunflower":
            sunflower()
        elif flower == "chrysanthemum":
            chrysanthemum()
        elif flower == "tulip":
            tulip()
        elif flower == "orchid":
            orchid()
        painter.penup()

def parse_input(user_input):
    tokens = re.findall(r'(\d+)?\s*([a-zA-Z]+)', user_input.lower())
    parsed_data = []
    unrecognized_flowers = set()
    
    for token in tokens:
        quantity = int(token[0]) if token[0] else 1 
        flower = token[1]
        if flower in flowerlist:
            parsed_data.append((flower, quantity))
        else:
            unrecognized_flowers.add(flower)
    
    if len(unrecognized_flowers) > 1:
        print(f"Unrecognized flowers: {', '.join(unrecognized_flowers)}")
        print("Suggested flowers: ", ', '.join(flowerlist))
    
    return parsed_data

johnsflowers = input("What would you like to draw? ")

parsedflowers = parse_input(johnsflowers)

if parsedflowers:
    for flower, quantity in parsedflowers:
        print(f"Drawing {quantity} {flower}(s)")
        drawflowers(flower, quantity)
else:
    print("No valid flowers found.")

t.done()
