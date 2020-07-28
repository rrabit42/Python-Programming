#이화여대 소프트웨어학부 사이버보안학과
#1871063 김서영



#사용자에게 점수 입력받기
test1 = int(input("첫번째 시험의 점수를 입력하시오: "))
test2 = int(input("두번째 시험의 점수를 입력하시오: "))
test3 = int(input("세번째 시험의 점수를 입력하시오: "))


#점수 합계 및 평균
sum = test1 + test2 + test3   #합계
average = sum/3               #평균




#자격증 합격 여부 판단하기
  #각 점수 60점 초과일 경우 혹은 점수 평균이 70점 이상일 경우 합격

if (test1>60 and test2>60 and test3>60) or (average>=70):
    print("\n자격증 시험에 합격하셨습니다.")
else:
    print("\n죄송합니다. 자격증 시험에 떨어지셨습니다.")
