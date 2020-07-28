#이화여대 소프트웨어학부 사이버보안학과
#1871063 김서영 



#사용자에게 숫자 입력받기
a = int(input("첫 번째 수를 입력하시오: "))
b = int(input("두 번째 수를 입력하시오: "))
c = int(input("세 번째 수를 입력하시오: "))


#가장 큰 수가 들어갈 변수 초기화
max = 0


#입력한 수 중에 가장 큰 수 판단
if a>b:
    if a>c:
        max = a
    else :
        max = c
else:
    if b>c:
        max = b
    else:
        max = c


#결과 출력
print("입력하신 값 %s,%s,%s중 가장 큰 수는 %s 입니다." %(a,b,c,max))
