"""

엘텍공과대학 소프트웨어학부
1871063 김서영

"""



import turtle

t = turtle.Turtle()

while (1):
    n = int(input("다각형을 만들 숫자를 입력하세요(3~30): "))
    if (3<=n<=30):
        break

for i in range(n):
    t.forward(100)
    t.left(360/n)
    
