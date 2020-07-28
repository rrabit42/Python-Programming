import turtle

t= turtle.Turtle()
heightLst = [120,56,309,220,23,98]

def drawBar(height):
    t.left(90)
    t.forward(height)
    t.right(90)
    t.forawrd(40)
    t.right(90)
    t.forward(height)


for i in range(len(heightLst)):
    heigth = heightLst[i]
    drawBar(height)
