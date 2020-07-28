"""
엘텍공과대학 사이버보안학과
1871063 김서영
"""

import turtle    #터틀 그래픽 모듈을 불러온다 
import random    #random 모듈을 불러온다 
import time      #time 모듈을 불러온다



#player 거북이 설정하기
player = turtle.Turtle()    #player 거북이 생성
player.color("blue")        #색
player.shape("turtle")      #모양
player.penup()              #움직일 때 선을 그리지 않도록 꼬리를 올린다
player.speed(0)             #속도
screen = player.getscreen() #player의 스크린 이벤트를 반환한다

#소행선1 설정하기
a1 = turtle.Turtle()        #소행성1 거북이 생성
a1.color("red")             #색
a1.shape("circle")          #모양
a1.penup()                  #꼬리를 올린다
a1.speed(0)                 #속도
a1.goto(random.randint(-300,300),random.randint(-300,300))  #좌표를 랜덤으로 설정한다

#소행선2 설정하기
a2 = turtle.Turtle()        #소행성2 거북이 생성
a2.color("red")             #색
a2.shape("circle")          #모양
a2.penup()                  #꼬리를 올린다
a2.speed(0)                 #속도
a2.goto(random.randint(-300,300),random.randint(-300,300))  #좌표를 랜덤으로 설정



#게임 진행에 필요한 함수들

  #왼쪽으로 돌기
def turnleft():
    player.left(30)   #player의 방향을 오른쪽으로 30도 회전

  #오른쪽으로 돌기
def turnright():
    player.right(30)  #plyaer의 방향을 왼쪽으로 30도 회전

  #스피드 조정
speed = 2          #처음 속도
def speedUp():
    global speed   #speed는 전역변수다
    speed += 1     #함수가 호출되면 speed를 1 올린다
    if speed == 6: #최대속도는 5이고, speed=5일 때 함수를 호출하면
        speed=2     #다시 속도는 처음(최저)속도로 돌아온다

  #위치 조정
def checkPosition():
    if a1.xcor()>500:   #소행성1의 x좌표가 500이 넘으면
        a1.goto(random.randint(-300,300),random.randint(-300,300)) #다시 랜덤으로 좌표 설정
    if a2.xcor()>500:   #소행성2의 x좌표가 500이 넘으면 
        a2.goto(random.randint(-300,300),random.randint(-300,300)) #다시 랜덤으로 좌표 설정
                        #player의 x,y좌표 중 하나라도 500이 넘으면
    if player.xcor()<-500 or player.xcor()>500 or player.ycor()<-500 or player.ycor()>500:
        player.goto(0,0) #player를 원점으로 돌려놓기

  #소행성1 격추하기
def destroy_1():
    if player.distance(a1)<12: #player와 소행성1의 거리가 12 미만이면
        a1.color("black")      #소행성1의 색은 검은색이 되고
        return 0               #0을 반환한다(나아가는 거리가 0이 됨, 즉 정지)
    else:
        return com1            #거리가 12 이상일 경우는 com1을 반환(com1=2, 즉 2씩 나아감)

  #소행성2 격추하기
def destroy_2():
    if player.distance(a2)<12: #player와 소행성2의 거리가 12미만이면
        a2.color("black")      #소행성2의 색은 검은색이 되고
        return 0               #0반환
    else:
        return com2            #그 외는 com2 반환



#키보드로 player조작하기
screen.onkeypress(turnleft,"Left")    #왼쪽방향키 누르면 turnleft() 호출
screen.onkeypress(turnright,"Right")  #오른쪽방향키 누르면 turnright() 호출
screen.onkeypress(speedUp,"space")    #space bar 누르면 speedUp() 호출
screen.listen()                       #player가 키보드 입력을 받는다



#게임 실행하기
  #소행성들이 움직이는 거리
com1 = 2
com2 = 2
  #게임 실행 함수
def play():
    player.forward(speed)            #speed만큼 거리를 움직인다
    global com1, com2                #com1,com2는 전역변수
    com1 = destroy_1()               #소행성1의 격추 여부 판단
    com2 = destroy_2()               #소행성2의 격추 여부 판단
    a1.forward(com1)                 #소행성1은 com1만큼 거리를 움직인다
    a2.forward(com2)                 #소행성2는 com2만큼 거리를 움직인다
    checkPosition()                  #거북이들의 거리를 확인 및 조정한다
    if (com1 == 0) and (com2 ==0):   #만약 소행성1,소행성2가 모두 격추되면(격추되면 정지되므로)
        end = time.time()            #끝나는 시간 기록
        et = end - start             #게임 플레이 시간 계산
        player.write("Finish : %0.2f" %et, False, "center", ("",15))  #player위치에 걸린 시간 출력
    else:
        move()                       #소행성들이 모두 격추되지 않았으면, 게임 반복(play(),move()함수가 반복적으로 호출된다)
   #게임 시작 및 지속 함수
def move():
    screen.ontimer(play,10)          #10ms가 지나면 play() 호출

start = time.time()                  #게임 시작 시간 기록
move()                               #게임 시작
