import turtle

def drawSquare(length):
    for i in range(4):
        t.forward(length)
        t.left(90)

def movePoint(x,y):
    t.up()
    t.goto(x,y)
    t.down()

t=turtle.Turtle()
t.shape("turtle")

movePoint(-200,0)
drawSquare(100)

movePoint(0,0)
drawSquare(100)

movePoint(200,0)
drawSquare(100)
