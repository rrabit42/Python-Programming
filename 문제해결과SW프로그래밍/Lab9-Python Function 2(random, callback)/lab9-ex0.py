"""
엘텍공과대학 소프트웨어학부 사이버보안학과
1871063 김서영
"""


import turtle
import random


t= turtle.Turtle()
t.shape("turtle")

for i in range(30):
    lenght = random.randint(1,100)
    t.forward(lenght)
    angle = random.randint(-180,180)
    t.right(angle)
    
