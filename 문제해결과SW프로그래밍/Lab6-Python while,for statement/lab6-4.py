#이화여대 소프트웨어학부 사이버보안과
#1871063 김서영




#turtle 관련 함수 사용
import turtle as t


#색 list 지정
color = ['yellow','red','green','purple','blue']


#원 순차적으로 그리기
for i in range(len(color)):
    t.up()
    t.goto(-200+i*100,0) #원 그릴 좌표
    t.down()

    t.width(3*(i+1))     #원 그릴 펜의 두께
    t.color(color[i])    #원의 색
    t.circle(10)         #지름이 10인 원 그리기
