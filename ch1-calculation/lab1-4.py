# 직각 삼각형 그리기

# 방법 1

import math  # 수학함수 사용
import turtle  # 터틀 그래픽 사용

t = turtle.Turtle()
t.shape("turtle")

t.forward(100)
t.left(90)
t.forward(100)
t.left(135)
t.forward(math.sqrt(100**2 + 100**2))


# 방법 2

import turtle  # 터틀 그래픽 사용

t = turtle.Turtle()
t.shape("turtle")

t.goto(100, 0)
t.goto(100,100)
t.goto(0,0)
