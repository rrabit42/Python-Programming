# 무지개빛 원을 그리는 터틀


import turtle
t = turtle.Turtle()
t.shape("turtle")

color_list = ["red", "yellow", "green", "blue", "purple", "red", "yellow", "green", "blue", "purple"]

for i in range(len(color_list)):    
    t.fillcolor(color_list[i])
    t.begin_fill()
    t.circle(50)
    t.end_fill()
    t.forward(30)






