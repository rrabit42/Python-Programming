import turtle

t = turtle.Pen()


##
##t.left(20)
##
##for i in range(4):
##    t.forward(50)
##    t.left(90)
##
##t.left(30)
##
##for i in range(4):
##    t.forward(50)
##    t.left(90)
##
##t.left(40)
##
##for i in range(4):
##    t.forward(50)
##    t.left(90)


n = 20

for i in range(3):
    t.left(20+10*i)
    for j in range(4):
        t.forward(50)
        t.left(90)
