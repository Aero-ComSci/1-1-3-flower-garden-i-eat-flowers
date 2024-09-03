import turtle as t
painter = t.Turtle()

flowerlist = ["Rose", "Sunflower", "Tulip", "Chrysanthemum", "Orchid"]
def rose():
    painter.pencolor("red")
    painter.forward(10)
    painter.circle(50)
    painter.forward(10)
    painter.circle(50)

def sunflower():
    painter.pencolor("yellow")
    painter.forward(10)

john = input('What do you want to draw?')
johnsplit = john.split()
flowerfound = False
coolset = set(flowerlist)
for word in johnsplit:
    if word in coolset:
        flowerfound = True
        print("Yippiee")
        painter.speed(0)
        if word == "Rose":
            rose()
if not flowerfound:
    print ("bum")

t.done()
