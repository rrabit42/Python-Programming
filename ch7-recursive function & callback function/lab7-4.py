def f(n) :
    if n <= 3 :
        return n
    else :
        return n + f(n-3)

n = int (input("숫자 : "))
n = n // 3 * 3
print(f(n))

