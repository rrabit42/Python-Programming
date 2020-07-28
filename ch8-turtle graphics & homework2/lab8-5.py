import turtle
import random

t = turtle.Turtle()
t.pensize(3)
colors = ["red", "yellow", "green", "blue", "purple", "pink"]
size = [30, 40, 50, 60, 70]

#원 그리는 함수
def drawCircle (c1, c2, radius) :
    t.color(c1, c2)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# (x, y) 지점으로 이동하는 함수
def move(x, y) :
    t.up()
    t.goto(x, y)
    t.down()

def draw(x, y) :
    move(x, y)
    c1 = random.choice(colors)
    c2 = random.choice(colors)
    length = random.choice(size)
    drawCircle(c1, c2, length)

s = turtle.Screen()
s.onscreenclick(draw)
