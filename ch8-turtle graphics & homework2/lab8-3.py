import turtle
import random

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
    
# 사각형 그리기
def drawRectangle(c1, c2, width) :
    t.color(c1, c2)
    t.begin_fill()
    for i in range (4) :
        t.forward(width)
        t.left(90)
    t.end_fill()

# 삼각형 그리는 함수
def drawTriangle(c1, c2, side) :
    t.color("purple", "pink")
    t.begin_fill()
    for i in range (3) :
        t.forward(100)
        t.left(120)
    t.end_fill()

# 그리는 작업
t = turtle.Turtle()
t.pensize(3)
colors = ["red", "yellow", "green", "blue", "purple", "pink"]

c1 = random.choice(colors)
c2 = random.choice(colors)
move(0, 0)  # (0, 0) 지점으로 이동
drawCircle(c1, c2, 50)  # 반지름 50인 원

c1 = random.choice(colors)
c2 = random.choice(colors)
move(100, 0) # (100, 0) 지점으로 이동
drawRectangle(c1, c2, 100) # 변이 100인 사각형

c1 = random.choice(colors)
c2 = random.choice(colors)
move(250, 0)    # (250, 0) 지점으로 이동
drawTriangle(c1, c2, 100) # 변이 100인 삼각형 

