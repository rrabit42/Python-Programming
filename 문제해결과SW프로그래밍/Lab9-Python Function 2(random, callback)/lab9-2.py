import turtle
import random

def drawSquare(length,color):
    t.begin_fill()
    t.fillcolor(color)
    for i in range(4):
        t.forward(length)
        t.left(90)
    t.end_fill()

def movePoint(x,y):
    t.up()
    t.goto(x,y)
    t.down()

t=turtle.Turtle()
t.shape("turtle")

for i in range(10):
    lenght = random.randint(50,100)
    color = random.choice(['green','black','yellow','red','blue'])
    x = random.randrange(-300,301)
    y = random.randrange(-200,201)
    movePoint(x,y)
    drawSquare(lenght,color)


