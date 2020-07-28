# 두 점을 잇는 선 그리기

import turtle
t = turtle.Turtle()
t.shape("turtle")

x1 = int (input("x1: "))
y1 = int (input("y1: " ))
x2 = int (input("x2: "))
y2 = int (input("y2: "))

t.up()
t.goto(x1, y1)
t.down()
t.goto(x2, y2)
