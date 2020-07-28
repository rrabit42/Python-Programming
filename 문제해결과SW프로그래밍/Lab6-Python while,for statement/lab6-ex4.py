n = int(input("양의 정수 입력: "))
tot = 0
i = 1

while(i<n):
    if i%3 == 0:
        tot+=i
    i+=1

print(tot)
