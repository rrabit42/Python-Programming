# 정수 입력 받기
n1 = int(input("정수 (1) : "))
n2 = int(input("정수 (2) : "))
n3 = int(input("정수 (3) : "))
n4 = int(input("정수 (4) : "))
n5 = int(input("정수 (5) : "))


# 최댓값, 최솟값 구하기
maxValue = max(n1, n2, n3, n4, n5)
minValue= min(n1, n2, n3, n4, n5)


# 결과 출력
print("최대값 = ", maxValue)
print("최소값 = ", minValue)
