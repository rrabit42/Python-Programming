n = int(input("행렬의 크기: "))
A = [[0 for j in range (n)] for i in range(n)]

for i in range (n) :
    for j in range (n):
        print("A[" + str(i) + "][" + str(j) + "] = ", end = "")
        A[i][j] = int (input())

for i in range (n) :
    for j in range (n) :
        print(A[i][j], end = "    ")
    print()

