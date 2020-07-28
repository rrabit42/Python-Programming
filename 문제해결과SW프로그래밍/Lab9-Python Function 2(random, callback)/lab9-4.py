'''
엘텍공대 소프트웨어학부 사이버보안
1871063 김서영
'''

def getGCD (x,y):
    total = 1
    if x<=y:
        min = x
    else:
        min = y
        
    for i in range(min+1,1,-1):
        if (x%i == 0) and (y%i == 0):
            total *= i
            x = x/i
            y = y/i
    return total


x = int(input("첫 번째 양의 정수 입력: "))
y = int(input("두 번째 양의 정수 입력: "))
result = getGCD(x,y)

print("최대공약수는 %s입니다." %result)
