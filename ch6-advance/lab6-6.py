n = int (input( "수열 위치: "))

if n == 0 or n == 1 :
    print(1)
else :
    a = 1
    b = 1
    for i in range (2, n+1) :
        f = a + b
        a = b
        b = f
    print(f)
