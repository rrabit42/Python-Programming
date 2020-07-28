import turtle

x1 = int(input("x1을 입력하세요: "))
y1 = int(input("y1을 입력하세요: "))
x2 = int(input("x2을 입력하세요: "))
y2 = int(input("y2을 입력하세요: "))

t= turtle.Turtle()
t.up()
t.goto(x1,y1)
t.down()
t.goto(x2,y2)

