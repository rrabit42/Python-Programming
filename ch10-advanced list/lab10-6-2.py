n = int(input())
A = [[i*n+j for j in range (n)] for i in range (n)]

for i in range (n) :
    for j in range (n):
        print(A[i][j], end = " ")
    print()
    
