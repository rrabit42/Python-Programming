import turtle

def turn_left(): # 왼쪽 화살표 누를 때 실행
    t.left(10)
    t.forward(10)

def turn_right(): # 오른쪽 화살표 누를 때 실행
    t.right(10)
    t.forward(10)

t = turtle.Turtle()
s = turtle.Screen()
t.shape("turtle")
t.speed(1) # 가장 느린 속도

#화살표 누를 때 할 일을 정한다
s.onkey(turn_left, "Left")
s.onkey(turn_right, "Right")

#이제 사용자의 입력을 기다린다
s.listen()  

