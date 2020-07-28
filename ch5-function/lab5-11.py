def isPrime(n) :
    for i in range (2, n//2 + 1) :
        if n % i == 0 :
            return False
    return True

n = int(input("양수 입력 : "))
if isPrime(n) :
    print("소수이다.")
else :
    print("소수가 아니다.")
