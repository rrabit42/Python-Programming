import turtle
import random
import time

t1 = turtle.Turtle()
t2 = turtle.Turtle()

t1.penup()
t1.goto(-300,0)

t2.penup()
t2.goto(-300,-100)

t1.color("pink")
t1.shape("turtle")
t1.shapesize(2)
t1.pensize(5)

t2.color("blue")
t2.shape("turtle")
t2.shapesize(3)
t2.pensize(5)

t1.pendown()
t2.pendown()

start = time.time()

for i in range(30):
    d1 = random.randint(1,50)
    t1.forward(d1)
    d2 = random.randint(1,50)
    t2.forward(d2)

end = time.time()
et = end - start

t1.write("Game Over: %0.2f" %et,False,"center",("",15))
