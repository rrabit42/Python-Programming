import turtle
t = turtle.Turtle( ) # 거북이 한마리
t.shape("turtle")    # 거북이 모양으로

t.width(5)            # 선의 굵기
t.color("red")        # 선의 색
t.circle(50)          # 원을 그리자

t.up()
t.goto(0, -25)
t.down()

t.width(10)
t.color("green")
t.circle(75)

t.up()
t.goto(0, -50)
t.down()

t.width(20)
t.color("blue")
t.circle(100)
