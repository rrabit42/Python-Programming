def f1(n) :
    if n == 1 :
        return 1
    else :
        return 2 + f1(n-1)

def f2(n) :
    if n == 1 :
        return 2
    else :
        return 2 + f2(n-1)

def f3(n) :
    if n == 1 :
        return 2
    else :
        return 3 + f3(n-1)    

def f4(n) :
    if n == 1 :
        return 1
    else :
        return 3 * f4(n-1)      

n = int(input("정수 입력: "))
print("f1의 n번째 수 = ", f1(n))
print("f2의 n번째 수 = ", f2(n))
print("f3의 n번째 수 = ", f3(n))
print("f4의 n번째 수 = ", f4(n))