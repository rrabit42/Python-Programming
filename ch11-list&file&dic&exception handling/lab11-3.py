# 파일의 숫자 읽어 합치기
f = open("d:\\infile.txt", "r")
sum = 0
for k in f :
    sum += int(k)
print(sum)


# 파일의 숫자들
file = open("d:\\infile.txt", "r") # 읽기용으로 열기 

for line in file : # 각 줄마다 ("\n" 포함하여) 읽어서
    print(line)   # 그대로 화면에 출력한다
file.close()

# 파일을 읽기용으로 다시 연다.
file = open("d:\\infile.txt", "r")
for line in file:  # 각 줄마다 ("\n" 포함하여) 읽지만
    print(int(line))   # 숫자로 변환하여 출력한다 
file.close()