def f(a, n) :
    if n == a :
        return n
    else :
        return n + f(a, n-a)

n = int(input("n = "))
a = int(input("a = "))
n = n // a * a
print(f(a, n))