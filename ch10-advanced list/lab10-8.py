n = int(input("행렬의 크기: "))

A = [[0 for j in range (n)] for i in range(n)]
B = [[0 for j in range (n)] for i in range(n)]
C = [[0 for j in range (n)] for i in range(n)]

print("행렬 A의 입력")
for i in range (n) :
    for j in range (n) :
        A[i][j] = int (input())

print("행렬 B의 입력")
for i in range (n) :
    for j in range (n) :
        B[i][j] = int (input())
        
for i in range (n) :
    for j in range (n) :
        C[i][j] = A[i][j] + B[i][j]
        
for i in range (n) :
    for j in range (n) :
        print(C[i][j], end = "    ")
    print()

