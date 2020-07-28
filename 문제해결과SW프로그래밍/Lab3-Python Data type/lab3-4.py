print("="*50)
print("     이화여자대학교 엘텍공과대학 소프트웨어학부")
print("               18학번 김서영")
print("="*50)

#커피를 각각 얼마나 팔았는지 입력 받는다.

Americano = int(input("아메리카노 판매 개수: ")) #아메리카노
CafeLatte = int(input("카페라떼 판매 개수: "))   #카페라떼
Cappuccino = int(input("카푸치노 판매 개수: "))  #카푸치노

#총 매출을 계산한다.
cash = Americano*2000 + CafeLatte*3000 + Cappuccino*3500

#결과화면을 출력한다.
print("총 매출은" + str(cash)+ " 입니다.")
