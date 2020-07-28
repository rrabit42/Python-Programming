def line(n) :
    for i in range (n) :
        print("*", end = "")
        
def triangle (n) :
    for i in range (1, n+1) :
        line(i)
        print()

triangle (7)