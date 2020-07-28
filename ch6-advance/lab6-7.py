n = int (input( "수열 위치: "))
fib = []

if n == 0 :
    fib.append(1)
    print(fib)
elif n == 1 :
    fib.append(1)
    fib.append(1)
    print(fib)
else :
    fib.append(1)
    fib.append(1)   
    for i in range (2, n+1) :
        fib.append(fib[i-2] + fib[i-1])
    print(fib)
