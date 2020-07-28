"""
엘텍공과대학 소프트웨어학부 사이버보안학과
1871063 김서영
"""


def factorial(n):
    total = 1
    for i in range(1,n+1):
        total *= i
    return total


n = int(input("팩토리얼을 구할 정수를 입력:"))

print("%s!은 %s입니다." %(n,factorial(n)))
