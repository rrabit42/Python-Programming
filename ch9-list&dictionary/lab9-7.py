def swap(A, i, j) :
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def moveMax(A, n) :
    index = 0
    max = A[0]
    for i in range (1, n) :
        if A[i] > max :
            max = A[i]
            index = i
    swap(A, index, n-1)

A = [50, 60, 20, 80, 40, 90, 0, 30, 10, 70]
print(A)
for i in range (len(A), 1, -1) :
    moveMax(A, i)
    print(A)

