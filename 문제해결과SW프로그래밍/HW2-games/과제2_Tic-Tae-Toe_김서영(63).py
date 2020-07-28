"""
엘텍공과대학 사이버보안학과
1871063 김서영
"""
#타임관련 함수를 import
import time




#게임판 제작(입력과 출력을 위해 list로)
board =[' ']*9


#게임보드 출력 함수
def drawBoard():
    print(" %c | %c | %c " %(board[0],board[1],board[2]))
    print("___|___|___")
    print(" %c | %c | %c " %(board[3],board[4],board[5]))
    print("___|___|___")
    print(" %c | %c | %c " %(board[6],board[7],board[8]))
    print("   |   |   ")


#게임의 진행 현황 조사(이겼는지, 비겼는지, 게임을 지속해야하는지)
def checkWin():
    
 #수평선상으로 같은 마크가 있는지 검사
    if (board[0] == board[1] and board[1] == board[2] and board[0] !=' '):
        return 2
    elif (board[3] == board[4] and board[4] == board[5] and board[3] != ' '):
        return 2
    elif (board[6] == board[7] and board[7] == board[8] and board[6] != ' '):
        return 2
    
 #수직선상에 같은 마크가 있는지 검사
    elif (board[0] == board[3] and board[3] == board[6] and board[6] != ' '):
        return 2
    elif (board[1] == board[4] and board[4] == board[7] and board[1] != ' '):
        return 2
    elif (board[2] == board[5] and board[5] == board[8] and board[2] != ' '):
        return 2
    
 #대각선상으로 이겼는지 검사
    elif (board[0] == board[4] and board[4] == board[8] and board[4] != ' '):
        return 2
    elif (board[2] == board[4] and board[4] == board[6] and board[4] != ' '):
        return 2
    
 #위의 경우가 아니면서 빈 셀이 아닌 경우 검사, 즉 비긴 경우
    elif (board[0] !=' ' and board[1] != ' ' and board[2] !=' ' and board[3] !=' ' and board[4] !=' ' and board[5] !=' ' and board[6] !=' ' and board[7] !=' ' and board[8] !=' '):
        return 1
    
 #위의 조건에 맞지 않으면 아직 빈 셀이 있는 경우임
    else:
        return 0





#게임 시작
print("Tic-Tac-Toe 게임 시작 (만든사람:김서영)") #게임이름 및 제작자
print("선수1 [X] --- 선수2 [0]\n")               #선수의 마크 설명
print()
print()
print("준비중입니다...")                         #게임 실행중...
time.sleep(3)                                    #3초 후에 게임 실행

  #보드판 출력
drawBoard()

  #게임 진행
gameCount=1                     #게임 횟수
win=0                           #게임 진행 여부 판단 변수

while True:                     #반복 실행(win == 0 일때)
    if (gameCount % 2 !=0):     #게임 횟수가 홀수일때는 선수1 차례
        print("선수1 차례")
        mark='X'                #선수1의 마크는 X
    else:
        print("선수2 차례")
        mark='O'                #선수2의 마크는 O
    position = int(input("마크하기를 원하는 위치(1~9)를 선택하세요: ")) #선수에게 표시할 위치 입력받기
    idx = position-1            #리스트에 위치 입력하기 위해 index 계산
    board[idx] = mark           #입력한 위치에 지정된 마크 표시
    drawBoard()                 #표시 후 다시 보드 출력
    
    win = checkWin()        #게임 진행 현황 조사 및 판단
    if (win==1):            #무승부일 경우
        print("무승부입니다.\n게임을 종료합니다.\n")
        break               #게임 종료
    elif (win==2):          #누군가 승리했을 경우
        if (gameCount %2 == 0 ):  #게임 횟수가 짝수이면
            print("선수2의 승리입니다.\n게임을 종료합니다.\n") #선수2가 마지막 마크를 표시했으므로 선수2 승리
            break           #게임 종료
        else:                     #게임 횟수가 홀수이면
            print("선수1의 승리입니다.\n게임을 종료합니다.\n") #선수1이 마지막 마크를 표시했으므로 선수1 승리
            break           #게임 종료
    gameCount +=1                #게임 종료가 아니면 게임 횟수 +1하고 게임 다시 반복


    
