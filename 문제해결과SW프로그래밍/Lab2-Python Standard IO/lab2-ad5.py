#김서영(1871063)

#위치 찾는 연습

import turtle
t = turtle.Turtle()

#원 그리기 (위치는 0,0)
t.width(10)          #선의 굵기
t.color("red")       #선의 색
t.circle(10)         #원을 그리자

#원 그리기 (위치는 100,0)
t.up()
t.goto(100,0)
t.down()

t.width(10)          #선의 굵기
t.color("blue")      #선의 색
t.circle(10)         #원을 그리자
