n = int (input("입력할 숫자의 개수: "))
A = [0 for i in range (n)]

for i in range (n):
    print("A[" + str(i) + "] = ", end = "")
    A[i] = int(input())

print(A)
