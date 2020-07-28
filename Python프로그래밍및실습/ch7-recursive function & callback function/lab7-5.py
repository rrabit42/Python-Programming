def f(n) :
    if n <= 2 :
        return n
    else :
        return n + f(n-2)

n = int(input("n = "))
print(f(n))
