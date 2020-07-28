def triangle2 (n) :
     for i in range (n) :
         for j in range (n-i) :
             print(" ", end = "")
         for j in range (i+1):
             print("*", end = "")
         print()

triangle2 (7)