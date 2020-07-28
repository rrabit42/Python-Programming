"""

엘텍공과대학 소프트웨어학부
1871063 김서영

"""


num = int(input("양의 정수를 입력하시오: "))

n1 = num//1000

num = num%1000

n2 = num//100

num = num%100

n3 = num//10

num = num%10

n4 = num

sum = n1+n2+n3+n4

print("자리수의 합은 %d입니다." %sum)
