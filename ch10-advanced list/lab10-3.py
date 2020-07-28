A = [40, 35, 70, 90, 15, 30, 20, 45, 25, 60]
print("최대값 찾기 전의 리스트 A")
print(A)

for i in range (len(A)-1):
    if A[i] > A[i+1] :
        t = A[i]
        A[i] = A[i+1]
        A[i+1] = t

print("최대값 찾은 후의 리스트 A")
print(A)
