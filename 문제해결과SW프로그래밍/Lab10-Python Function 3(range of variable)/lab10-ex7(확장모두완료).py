import turtle
import random

player = turtle.Turtle()
player.color("blue")
player.shape("turtle")
player.penup()
player.speed(0)
screen=player.getscreen()


a1 = turtle.Turtle()
a1.color("red")
a1.shape("circle")
a1.penup()
a1.speed(0)
a1.goto(random.randint(-300,300),random.randint(-300,300))

a2 = turtle.Turtle()
a2.color("red")
a2.shape("circle")
a2.penup()
a2.speed(0)
a2.goto(random.randint(-300,300),random.randint(-300,300))


def turnleft():
    player.left(30)

def turnright():
    player.right(30)

speed = 2
def speedUp():
    global speed
    speed += 1
    if speed == 6:
        speed=2
    return speed
    
def checkPosition():
    if a1.xcor()>500:
        a1.goto(random.randint(-300,300),random.randint(-300,300))
    if a2.xcor()>500:
        a2.goto(random.randint(-300,300),random.randint(-300,300))
    if player.xcor()<-500 or player.xcor()>500 or player.ycor()<-500 or player.ycor()>500:
        player.goto(0,0)


screen.onkeypress(turnleft,"Left")
screen.onkeypress(turnright,"Right")
screen.onkeypress(speedUp,"space")
screen.listen()

def play():
    player.forward(speed)
    a1.forward(2)
    a2.forward(2)
    checkPosition()
    move()

def move():
    screen.ontimer(play,10)

move()
