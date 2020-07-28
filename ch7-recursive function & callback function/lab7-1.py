def f(n) :
    print("f : ", n)
    return n * g(n-1)


def g(n) :
    print("g : ", n)
    return n * h(n-1)

def h(n) :
    print("h : ", n)
    return n

print(f(3))
    
