# moveMax를 사용한 버블 정렬
A = [40, 35, 70, 90, 15, 30, 20, 45, 25, 60]
print("정렬 전의 리스트 A")
print(A)

def moveMax(A, n):
    for i in range (n-1):
        if A[i] > A[i+1] :
            t = A[i]
            A[i] = A[i+1]
            A[i+1] = t

for i in range (len(A)-1):
  moveMax(A, len(A)-i)

print("정렬 후의 리스트 A")
print(A)

# nested for loop만 쓰는 버블 정렬
A = [40, 35, 70, 90, 15, 30, 20, 45, 25, 60]
print(A)

for j in range (len(A)-1):
    for i in range (len(A) - j - 1):
        if A[i] > A[i+1] :
            t = A[i]
            A[i] = A[i+1]
            A[i+1] = t
            
print(A)
