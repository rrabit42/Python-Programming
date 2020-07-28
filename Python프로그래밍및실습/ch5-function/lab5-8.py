def line(n) :
    for i in range (n) :
        print("*", end = "")

def blankline(n) :
    for i in range (n) :
        print(" ", end = "")

def parallelogram (n) :
     for i in range (n) :
         blankline(n-i-1)
         line(n)
         print()

parallelogram (7)