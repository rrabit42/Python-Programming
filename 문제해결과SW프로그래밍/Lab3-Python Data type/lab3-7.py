print("="*50)
print("     이화여자대학교 엘텍공과대학 소프트웨어학부")
print("               18학번 김서영")
print("="*50)

#사용자로부터 값을 입력 받는다.

 #투입한 돈
money = int(input("투입한 돈: "))

 #물건 값
product = int(input("물건값(100원 단위) : "))



#거스름돈을 계산한다.
left = money - product

#거스름돈 값을 출력한다.
print("거스름돈: ",left)



#거슬러 줄 동전의 개수를 계산한다.

 #500원 동전의 개수
bill_5 = left //500

 #100원 동전의 개수
bill_1 = left%500//100


#동전개수 출력
print("500원 동전의 개수: ",bill_5)
print("100원 동전의 개수: ",bill_1)

