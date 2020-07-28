def isEven(n) :
    if n % 2 == 0 :
        return True
    else :
        return False

n = int(input("숫자 입력 : "))
if isEven(n) :
    print("짝수")
else :
    print("홀수")