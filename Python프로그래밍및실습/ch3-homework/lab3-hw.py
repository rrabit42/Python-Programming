import turtle
import math
t=turtle.Turtle()                                       #거북이 한마리
t.shape("turtle")                                       #거북이 모양으로



#삼각형을 그리기 위해 필요한 변수 지정
width = int(input("삼각형의 밑변: "))                   #밑변의 길이
height = int(input("삼각형의 높이: "))                  #높이
num= int(input("삼각형의 개수: "))                      #그릴 삼각형의 개수
list= ["yellow","green", "blue", "purple", "red"]       #삼각형에 칠하고 싶은 색들

theta = math.atan(height/width)                         #각 구하기(라디안)
degree = theta*180/math.pi                              #각 변환
slope = math.sqrt(height**2+width**2)                   #빗변의 길이 변수 지정


t.fillcolor(list[4])                                    #첫번째 삼각형 색 지정
t.begin_fill()                                          #색 채우기 시작
t.forward(width)                                        #밑변 그리기
t.left(90)                                              #거북이 머리 회전
t.forward(height)                                       #높이 그리기
t.left(90+degree)
t.forward(slope)
t.end_fill()                                            #색 채우기 끝
t.backward(slope)                                       #빗변 길이 만큼 뒤로 돌아가기

for i in range (num-1) :                                #삼각형 반복해서 그리기
    t.begin_fill()
    t.fillcolor(list[i%5])
    t.right(90)
    t.forward(height)
    width = math.sqrt(height**2+width**2)               #빗변길이가 새로운 삼각형의 밑변이 되기위한 변수 재정의
    new_theta = math.atan(height/width)                 #새 밑변길이에 따른 새로운 라디안 각 정의
    new_degree = new_theta*180/math.pi                  #새 라디안 각에 따른 각 변화 다시
    new_slope = math.sqrt(height**2+width**2)           #새 밑변길이에 따른 새로운 빗변 길이 정의
    t.left(90+new_degree)
    t.forward(new_slope)
    t.end_fill()
    t.backward(new_slope)
