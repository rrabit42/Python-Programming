"""

엘텍공과대학 소프트웨어학부
1871063 김서영

"""



import turtle

t = turtle.Pen()
t.color("blue")
t.begin_fill()
for i in range(5):
    t.forward(100)
    t.right(144)
t.end_fill()
