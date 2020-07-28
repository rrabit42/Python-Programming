n = int(input("양의 정수 입력 : "))
tot = 0

while(n>0):
    if n%3 == 0:
        tot +=n
    n-=1

print(tot)
