"""
엘텍공과대학 소프트웨어학부 사이버보안학과
1871063 김서영
"""


import turtle
t = turtle.Turtle()

def drawFigure(n):
    if n==1:
        for i in range(3):
            t.forward(100)
            t.left(60)
    elif n==2:
        for i in range(4):
            t.forward(100)
            t.left(90)
    elif n==3:
        for i in range(5):
            t.forward(100)
            t.left(360/5)


n = int(input("숫자를 입력하세요(1~3):"))
while n<1 or n>3:
    print("1~3 숫자로 다시 입력하세요")
    n = int(input("숫자를 입력하세요(1~3):"))

drawFigure(n)
