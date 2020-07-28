import turtle #터틀 그래픽 모듈을 불러온다


playing = False #변수의 값이 False면 게임 끝, True면 게임 시작


t= turtle.Turtle() #미로 그릴 터틀 지정
s=turtle.Screen()

t.shape("turtle") #모양은 거북이
t.speed(0) #가장 빠른 스피도


player = turtle.Turtle() #플레이할 터틀 지정
image1 = "C:\\Users\\김서영\\Desktop\\캐릭터.gif" #플레이어 사진으로 쓸 이미지 지정
s.addshape(image1)
player.shape(image1)



def turn_left(): #왼쪽화살표 누를때 실행
    player.left(10)
    player.forward(10)

def turn_right(): #오른쪽 화살표 누를때 실행
    player.right(10)
    player.forward(10)

def maze(x,y): #(x,y)위치에 미로그리기 실행
    for i in range(2):
        t.penup()
        if i==1:
            t.goto(x+100,y+100)
        else:
            t.goto(x,y)
        t.pendown()
        t.forward(300)
        t.right(90)
        t.forward(300)
        t.left(90)
        t.forward(300)



def start(): #게임 시작
    global playing
    if playing==False:
        playing == True
        player.clear() #과거 플레이어가 지나간 흔적 모두 지운다
        play()


def play(): #게임 진행중
    global playing
    maze(-300,200) #미로를 그린다
    player.penup()
    player.goto(-300,250) #플레이어의 출발 위치
    player.speed(1)
    player.pendown()
    (x1,y1) = player.pos()
    if player.pos() == t.pos(): #미로와 플레이어가 서로 닿을때
        print("경로를 이탈하셨습니다. 실패")
        playing == False
    elif x1==400 and -100<=y1<=0 : #미로에 닿지 않고 플레이어가 골인 지점에 도착했을 때
        print("미로를 무사히 탈출하셨습니다. 성공")

s.onkey(start,'space') #스페이스바를 누르면 게임 시작
s.onkey(turn_left,"Left") #왼쪽 화살표 누를 때 할 일을 정한다
s.onkey(turn_right,"Right") #오른쪽 화살표 누를 때 할 일을 정한다
s.listen() #사용자의 입력을 기다린다



#제가 만드려는 게임에서 결과가 나오려면 미로와 플레이어가 닿느냐가 중요합니다.
#그래서 좌표를 이용해 결과를 출력하고자 했는데 좌표반환 함수는 배우지 않아서 검색을 통해 알아내었습니다.
#그런데 이 함수를 이용해 변수를 지정해서 조건식을 입력하고 싶은데 잘 몰라서 제대로 작동이 되질 않아요ㅠ
#실행하면 오류는 없다고 떠서 이유를 모르겠습니다.
#제 지식 밖이라 그냥 그대로 제출합니다...ㅠㅠㅠㅠ
#그냥 어떤 식으로 짜려고 했구나 정도만 봐주셨으면 합니다..!


