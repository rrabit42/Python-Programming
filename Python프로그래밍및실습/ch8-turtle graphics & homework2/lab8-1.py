import turtle
t = turtle.Turtle()
t.pensize(3)

#원 그리기
t.color("green", "yellow")
t.begin_fill()
t.circle(50)
t.end_fill()

# 사각형 그릴 곳으로 이동
t.up()
t.goto(100, 0)
t.down()

# 사각형 그리기
t.color("blue", "red")
t.begin_fill()
for i in range (4) :
    t.forward(100)
    t.left(90)
t.end_fill()

# 삼각형 그릴 곳으로 이동
t.up()
t.goto(250, 0)
t.down()

#삼각형 그리기
t.color("purple", "pink")
t.begin_fill()
for i in range (3) :
    t.forward(100)
    t.left(120)
t.end_fill()
