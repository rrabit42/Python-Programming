def swap(A, i, j) :
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

A = [50, 10, 20, 80, 40, 90, 0, 30, 60, 70]

def moveMax(A, n) :
    index = 0
    max = A[0]
    for i in range (1, n) :
        if A[i] > max :
            max = A[i]
            index = i
    if index != 0 :
        swap(A, index, n-1)

print(A)
moveMax(A, len(A))
print(A)
