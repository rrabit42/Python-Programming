import turtle
t = turtle.Turtle()
t.shape("turtle")

radius = int (input ("원의 반지름 : "))
distance = int (input("원 사이의 거리 : "))
n = int (input("원의 개수: "))

colors = ["red", "yellow", "green"]

for i in range (n):
    t.fillcolor(colors[i%3])
    t.begin_fill()
    t.circle(radius)
    t.up()
    t.forward(distance)
    t.down()
    t.end_fill()