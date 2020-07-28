#김서영(1871063)


import turtle
t = turtle.Turtle()


#빨간색 원 그리기

t.color("red")
t.width(10)
t.circle(10)

#위치 이동해서 파란색 원 그리기

 #위치 이동위해 펜 띄워서 이동시키기
t.penup()
t.goto(100,0)
t.pendown()

t.color("blue")
t.width(10)
t.circle(10)



#보라색 원 그리기

t.penup()
t.goto(0,100)
t.pendown()

t.color("purple")
t.width(10)
t.circle(10)



#초록색 원 그리기

t.penup()
t.goto(-100,0)
t.pendown()

t.color("green")
t.width(10)
t.circle(10)



#노락색 원 그리기

t.penup()
t.goto(0,-100)
t.pendown()

t.color("yellow")
t.width(10)
t.circle(10)
