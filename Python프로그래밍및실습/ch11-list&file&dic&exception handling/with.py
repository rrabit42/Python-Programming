f = open("d:\\myfile.txt", "w")  # 파일 열기
f.write("안녕하세요? \n")         # 파일에 쓰기
f.close( )                              # 파일 닫기

# with 안에서 파일을 사용한다. 별도로 닫을 필요가 없다.
with open("d:\\myfile.txt", "w") as f:
    f.write("안녕하세요? \n")

# 여러 파일 동시에 열고 쓰기
with open("d:\\infile.txt", "r") as f1, open("d:\\outfile.txt", "w") as f2 :
    data = f1.readline( )
    f2.write(data)

