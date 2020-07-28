import random

file = open("d:\\random.txt", "w")  # 저장하기

for i in range (50) :
    num = str(random.randint(1, 100)) + " "
    file.write(num)

file.close()

file = open("d:\\random.txt", "a")  # 추가하기

for i in range (30) :
    num = str(random.randint(101, 200)) + " "
    file.write(num)
    
file.close()
