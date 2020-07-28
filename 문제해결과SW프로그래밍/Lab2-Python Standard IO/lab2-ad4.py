#김서영(1871063)


#원을 그리는 연습

import turtle
t= turtle.Turtle()
t.shape("turtle")

#맨 안에 있는 원 그리기
t.width(5)
t.color("red")
t.circle(50)

#중간에 있는 원 그리기
t.width(10)
t.color("green")
t.circle(75)

#밖에 있는 원 그리기
t.width(20)
t.color("blue")
t.circle(100)

#마지막 커서 (거북이)를 이동시켜 보았음
t.width(1)
t.forward(100)
