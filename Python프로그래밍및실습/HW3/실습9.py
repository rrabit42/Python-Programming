s = {}
s['변영신'] = [[70, 80, 90], [60, 70, 80, 85, 90], [90, 80]]
s['이하영'] = [[70, 80, 60, 80], [70, 50, 60], [100, 90, 80, 60, 70]]
s['지수연'] = [[90, 80, 90], [70, 90], [80, 60, 70, 50], [90, 90, 80]]

infile = open("D:\\scores.txt", "r")  # 파일을 읽기모드로 연다
student = infile.readline()  # 학생 1명의 정보를 읽음
stlist = student.split()
name = stlist[0]  # 학생 이름을 name에 저장

print(name)  # 학생 이름 출력

del stlist[0]  # 학생 이름을 리스트에서 삭제

print("원래점수: ", s[name])  # 원래 점수 출력

# stlist의 입력점수를 숫자로 변환한 새 리스트 intlist만듬
intlist = []
for i in range(len(stlist)):
    intlist.append(int(stlist[i]))

print("입력점수 : ", intlist)  # 추가 점수 출력

s[name].append(intlist)

print("추가후 점수: ", intlist)  # intlist 추가한 리스트 출력

infile.close()  # 할일이 끝났으므로 파일을 닫는다