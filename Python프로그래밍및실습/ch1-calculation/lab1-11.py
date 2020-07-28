# 계단 그리기

import turtle
t = turtle.Turtle( )
t.shape("turtle")

height = int(input("계단 높이: "))
width = int(input("계단 너비: "))
num = int(input("계단 개수: "))

for i in range (num) :
    t.left(90)
    t.forward(height)
    t.right(90)
    t.forward(width)

    

