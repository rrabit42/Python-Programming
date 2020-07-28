n = int(input("행의 수: "))
A = [[i*n+j for j in range (n)] for i in range (n)]

for i in range (n) :
    for j in range (n):
        print("{0:7}" .format(A[i][j]), end = "")  #0번째 아이템을 7칸에 출력
    print()