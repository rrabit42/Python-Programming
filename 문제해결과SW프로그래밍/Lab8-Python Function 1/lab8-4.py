"""
엘텍공과대학 소프트웨어학부 사이버보안학과
1871063 김서영
"""


def factorial(n):
    total = 1
    for i in range(1,n+1):
        total *= i
    return total

while (1):
    n = int(input("팩토리얼을 구할 정수를 입력(0은 종료):"))
    if n == 0:
        print("프로그램을 종료합니다.\n")
        break
    elif n<0:
        print("양의 정수를 입력하세요\n")
    else:
        print("%s!은 %s입니다.\n" %(n,factorial(n)))
