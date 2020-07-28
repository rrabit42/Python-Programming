#이화여대 소프트웨어학부 사이버보안학과
#1871063 김서영



#사용자에게 정보 입력받기
pencil = int(input("연필 개수 입력: "))
pen = int(input("볼펜 개수 입력: "))


#금액 계산위한 변수 지정 및 초기화
sum = pencil*1000 + pen*2000


#금액 계산 및 결과 출력
if sum>10000:                       #총 금액이 만원 이상일 경우 10% 할인
    sum = sum*0.9
    print("\n10% 할인되었습니다.")
    print("지불할 돈: %d원" %sum)
else:
    print("\n지불할 돈: %d원" %sum)
