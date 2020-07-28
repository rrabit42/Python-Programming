# 모든 원소가 0으로 초기화된 5x4 행렬
A = [[0 for j in range (4)] for i in range (5)]

# 행렬 전체 출력
print(A)
print()

# 행렬을 행 단위로 출력
for i in range (5):
    print(A[i])
print()

# 행렬을 원소 단위로 출력
for i in range (5):
    for j in range (4):
        print(A[i][j], end = " ")
    print()


