#김서영(1871063)

#사용자에게서 찾고자 하는 돈의 액수 입력 받기

money = int(input("인출 금액(1천 단위 이상으로): "))

print()
print("="*30)

#거슬러줄 5만원의 개수
fivem = money //50000

#거슬러줄 1만원의 개수

a = money%50000
onem = a//10000

#거슬러줄 5천원의 개수

b = a%10000
fivet = b//5000

#거슬러줄 1천원의 개수

c = b%5000
onet = c//1000


#결과문 출력하기

print("5만원 -", fivem,"장")
print("1만원 -", onem,"장")
print("5천원 -", fivet,"장")
print("1천원 -", onet,"장")
