#김서영(1871063)



print("*"*30)

#사용자에게 거스름돈을 입력받아 정수로 변환한다
n = int(input("거스름돈을 입력하세요: "))

#거슬러줄 100원짜리 동전 개수
a = n//100

#거슬러줄 50원짜리 동전 개수
b = n%100
c = b//100

#거슬러줄 10원짜리 동전 개수
d = b%50
e = d//10

print()
print("="*30)
print("100원 동전 개수",a)
print("50원 동전 개수",c)
print("10원 동전 개수",e)
