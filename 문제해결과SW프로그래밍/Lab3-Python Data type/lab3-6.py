print("="*50)
print("     이화여자대학교 엘텍공과대학 소프트웨어학부")
print("               18학번 김서영")
print("="*50)

#사용자로부터 몸무게를 입력받는다.
weight = float(input("몸무게를 kg 단위로 입력하시오: "))

#키도 입력받는다.
height = float(input("키를 미터 단위로 입력하시오: "))

#주어진 식을 이용해 BMI를 계산한다.
BMI = weight/(height**2)


#결과화면 출력
print("당신의 BMI =",BMI)
