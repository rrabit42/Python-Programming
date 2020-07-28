#이화여대 소프트웨어학부 사이버보안학과
#1871063 김서영



#사용자에게 정보 입력받기
name = input("이름을 입력하시오: ")
score= int(input("점수를 입력하시오: "))


#학점 변수 초기화
grade = '0'


#점수에 따라 학점 판단하기
if 90<=score<=100:
    grade = 'A'
elif 80<=score<90:
    grade = 'B'
elif 70<=score<80:
    grade = 'C'
elif 60<=score<70:
    grade = 'D'
elif 0<=score<60:
    grade = 'F
else:
    print("점수를 잘못 입력하셨습니다.")   #0~100사이의 점수가 아닐 경우


#결과 출력
print("%s 학생의 학점은\n\"%s학점\"입니다." %(name,grade))
