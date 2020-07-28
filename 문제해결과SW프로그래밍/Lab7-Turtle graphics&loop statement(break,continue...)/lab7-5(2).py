"""

엘텍공과대학 소프트웨어학부
1871063 김서영

"""


num = int(input("양의 정수를 입력하시오: "))

sum = 0

a = len(str(num))

for i in range(a):
    n = num//10*(a-(i+1))
    num = num%10*(a-(i+1))
    if 0<num<=9:
        n = num
    sum +=n

print("자리수의 합은 %d입니다." %sum)
    
