import turtle

def drawSquare(length):
    for i in range(4):
        t.forward(length)
        t.left(90)

def movePoint(x,y):
    t.up()
    t.goto(x,y)
    t.down()

def drawIt(x,y):
    movePoint(x,y)
    drawSquare(100)

t=turtle.Turtle()
t.shape("turtle")

drawIt(-200,0)

drawIt(0,0)

drawIt(200,0)
