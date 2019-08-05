import turtle
t = turtle.Turtle( ) # 거북이 한마리
t.shape("turtle")    # 거북이 모양으로

# 맨 안에 있는 원 그리기
t.width(5)           # 선의 굵기
t.color("red")       # 선의 색
t.circle(50)         # 원을 그리자

# 중간에 있는 원 그리기
t.width(10)
t.color("green")
t.circle(75)

# 밖에 있는 원 그리기
t.width(20)
t.color("blue")
t.circle(100)

# 마지막 커서 (거북이)를 이동시켜 보았음
t.width(1)
t.forward(100)
