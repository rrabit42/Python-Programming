import turtle
import random

def drawSquare():
    length = random.randint(50,100)
    for i in range(4):
        t.forward(length)
        t.left(90)

def movePoint():
    x = random.randrange(-300,301)
    y = random.randrange(-200,201)
    t.up()
    t.goto(x,y)
    t.down()

t=turtle.Turtle()
t.shape("turtle")

for i in range(10):
    movePoint()
    drawSquare()


''' or

import turtle
import random

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

for i in range(10):
    length = random.randint(50,100)
    x = random.randrange(-300,301)
    y = random.randrange(-200,201)
    movePoint(x,y)
    drawSquare(length)


'''
