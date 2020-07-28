file = open("d:\\infile.txt", "r")

for line in file :
    line = line.split()
    sum = 0  # 줄 단위로 합계 계산
    for num in line :
        sum += int (num)
    print(sum)
