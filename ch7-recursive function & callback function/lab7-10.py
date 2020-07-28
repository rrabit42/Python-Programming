def hanoi(n) :
    if n==1 :
        return 1
    else :
        return hanoi(n-1) + 1 + hanoi(n-1)

n = int(input("원반의 개수 : "))
print(hanoi(n))
