import turtle
t = turtle.Turtle( ) # 거북이 한마리

# 원 그리기  (위치는 0, 0)
t.width(10)           # 선의 굵기
t.color("red")       # 선의 색
t.circle(10)         # 원을 그리자


# 원 그리기  (위치는 100, 0)
t.up()
t.goto(100,0)
t.down()

t.width(10)           # 선의 굵기
t.color("blue")       # 선의 색
t.circle(10)         # 원을 그리자

# 원 그리기  (위치는 -100, 0)
t.up()
t.goto(-100,0)
t.down()

t.width(10)           # 선의 굵기
t.color("green")       # 선의 색
t.circle(10)         # 원을 그리자

# 원 그리기  (위치는 0, 100)
t.up()
t.goto(0, 100)
t.down()

t.width(10)           # 선의 굵기
t.color("purple")       # 선의 색
t.circle(10)         # 원을 그리자

# 원 그리기  (위치는 0, -100)
t.up()
t.goto(0, -100)
t.down()

t.width(10)           # 선의 굵기
t.color("yellow")       # 선의 색
t.circle(10)         # 원을 그리자
