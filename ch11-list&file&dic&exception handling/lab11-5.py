f1 = open("d:\\infile1.txt", "r")
f2 = open("d:\\infile2.txt", "r")
for i in range (5) :
    n1 = int(f1.readline())
    n2 = int(f2.readline())
    print(n1+n2)
    
f1.close()
f2.close()
