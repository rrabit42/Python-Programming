import turtle

t = turtle.Turtle()
t.shape("turtle")

radius = int(input("원의 반지름 : "))
distance = int(input("원 사이의 거리 : "))
n = int(input("원의 개수: "))

for i in range(n):
    t.circle(radius)
    t.up()
    t.forward(distance)
    t.down()
