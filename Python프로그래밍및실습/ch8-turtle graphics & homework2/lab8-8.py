import turtle
def turn_left(): # 왼쪽 화살표 누를 때 실행
    t1.left(10)
    t1.forward(10)

def turn_right(): # 오른쪽 화살표 누를 때 실행
    t1.right(10)
    t1.forward(10)

def turn_up(): # 위쪽 화살표 누를 때 실행
    t2.left(10)
    t2.forward(10)

def turn_down(): # 위쪽 화살표 누를 때 실행
    t2.right(10)
    t2.forward(10)

def move(t, x, y) :
    t.up()
    t.goto(x, y)
    t.down()    
    
s = turtle.Screen()
image1 = "c:\\Users\\Myung\\Desktop\\rabbit.gif"
image2 = "C:\\Users\\Myung\\Desktop\\turtle.gif"
s.addshape(image1)
s.addshape(image2)

# 거북이 1
t1 = turtle.Turtle()
t1.shape(image1)
move(t1, 0, 0)
t1.speed(1)

#거북이 2
t2 = turtle.Turtle()
t2.shape(image2)
move(t2, 0, -100)
t2.speed(1)


#화살표 누를 때 할 일을 정한다
s.onkey(turn_left, "Left")
s.onkey(turn_right, "Right")
s.onkey(turn_up, "Up")
s.onkey(turn_down, "Down")

#이제 사용자의 입력을 기다린다
s.listen()  

