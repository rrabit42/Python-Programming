def line(n) :
    for i in range (n) :
        print("*", end = "")

def blankline(n) :
    for i in range (n) :
        print(" ", end = "")

def triangle3 (n) :
     for i in range (n) :
         blankline(n-i)
         line(i+1)
         print()

triangle3 (7)