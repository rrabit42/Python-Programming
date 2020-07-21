import turtle
import math

t = turtle.Turtle()
t.shape("turtle")

width = int (input ("밑변 : "))
height = int (input("높이 : "))

t.forward(width)
t.left(90)
t.forward(height)
slope = math.sqrt(width**2 + height**2)
degree = math.atan(height/width)*180/math.pi + 90
t.left(degree)
t.forward(slope)
