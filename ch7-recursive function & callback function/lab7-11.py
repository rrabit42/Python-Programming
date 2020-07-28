import turtle
def square(length) :
    for i in range (4) :
        t.forward (length)
        t.left (90)

def circle (length) :
    t.circle(length)

def draw(x, y) :
    global count

    t.up()
    t.goto(x, y)
    t.down()

    if count % 2 == 0 :
        t.color("green")
        t.begin_fill()
        square(50)
        t.end_fill()
        count += 1
    else :
        t.color("red")
        t.begin_fill()
        t.circle(25)
        t.end_fill()
        count += 1

t = turtle.Turtle()
s = turtle.Screen()
count = 0
s.onscreenclick(draw)
