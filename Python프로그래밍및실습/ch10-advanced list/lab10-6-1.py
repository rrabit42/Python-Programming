n = 3

# 행렬 A의 각 원소를 0으로 초기화
A = [[0 for j in range (n)] for i in range (n)] # n행 n 열의 행렬

# 행렬 A의 각 원소에 n 을 대입
for i in range (n) :
    for j in range (n):
        A[i][j] = n

# 행렬 B의 각 원소를 n 으로 직접 초기화
B = [[n for j in range (n)] for i in range (n)]

