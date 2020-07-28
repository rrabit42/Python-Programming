A = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(A)

for i in range (len(A)) :
    print(A[i], end = " ")
print()
    
B = [0 for i in range (5)]
print(B)

for i in range (len(B)):
    B[i] = i
    print(B[i], end = " ")
print()
