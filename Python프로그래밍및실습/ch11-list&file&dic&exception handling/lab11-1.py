import random

n1 = int (input("난수의 범위1 : "))
n2 = int (input("난수의 범위2 : "))
n = int (input("난수의 개수 : "))

R = [0 for i in range (n)]
for i in range (len(R)) :
    R[i] = random.randint(n1, n2)
print(R)
