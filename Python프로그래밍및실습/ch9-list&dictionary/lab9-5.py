def swap(A, i, j) :
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

A = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
i = int (input("숫자1: "))
j = int (input("숫자2: "))
swap(A, i, j)
print(A)
