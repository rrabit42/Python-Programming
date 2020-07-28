def line(n) :
    for i in range (n) :
        print("*", end = "")
        
def rectangle (n) :
    for i in range (n) :
        line(n)
        print()

rectangle (7)