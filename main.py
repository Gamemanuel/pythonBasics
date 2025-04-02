import turtle
t = turtle.Turtle()

def shapes(numberOfSides, lengthOfSides):
    angle = 360 / numberOfSides
    for _ in range(numberOfSides):
        t.forward(lengthOfSides)
        t.right(angle)

shapes(3, 100)
turtle.done() # makes the window stay open