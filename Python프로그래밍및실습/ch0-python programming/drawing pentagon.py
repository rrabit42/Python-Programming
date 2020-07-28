import turtle
t = turtle.Turtle()
t.shape("turtle")

radius = 90
t.width(10)

t.up()
t.goto(-150, 0)
t.down()

t.color("blue")
t.circle(radius)

t.up()
t.goto(0, 0)
t.down()

t.color("black")
t.circle(radius)

t.up()
t.goto(150, 0)
t.down()

t.color("red")
t.circle(radius)

t.up()
t.goto(-80, -100)
t.down()

t.color("yellow")
t.circle(radius)

t.up()
t.goto(80, -100)
t.down()
t.color("green")
t.circle(radius)
