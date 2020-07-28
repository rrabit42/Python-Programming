print("학생별 학기별 원점수 (가나다순): ")

file = open("C:\\Users\\김서영\Desktop\\scores.txt", "r")  # 파일을 읽기모드로 열기 검토를 위해 직접 노트북에 깔았기 때문에 좌표가 학생의 노트북으로 되어있음

# 각 학생의 점수 집합을 담을 list를 만듬
list_b = []
list_l = []
list_g = []

# 각 학생의 점수 집합을 만든다
for line in file:
    list = []
    line = line.split()  # 각 줄을 단어로 쪼갠다
    name = line[0]  # 첫번째 단어는 이름이다
    del line[0]  # 이름은 점수집합과 관련없으므로 delete한다
    if name == "변영신":  # 변영신의 점수만 모으도록
        for word in line:
            list.append(int(word))  # list속 단어들을 모두 정수로 바꾼다
        list_b.append(list)
    elif name == "이하영":
        for word in line:
            list.append(int(word))
        list_l.append(list)
    elif name == "지수연":
        for word in line:
            list.append(int(word))
        list_g.append(list)

# 문제에서 원하는 바를 출력한다
print("변영신", end=" ")
print(list_b)
print("이하영", end=" ")
print(list_l)
print("지수연", end=" ")
print(list_g)

print()

print("학생별, 학기별 평균 점수(가나다순) :")
print("변영신")

# 학기별 평균을 구한다
for i in range(len(list_b)):
    C = sum(list_b[i]) / len(list_b[i])  # 이게 평균 구한 식
    print("   ", i + 1, "학기", "%5.2f" % C)  # 소수점 둘째자리까지 나오도록

print()

print("이하영")  # 이하동문
for i in range(len(list_l)):
    C = sum(list_l[i]) / len(list_l[i])
    print("   ", i + 1, "학기", "%5.2f" % C)

print()

print("지수연")
for i in range(len(list_g)):
    C = sum(list_g[i]) / len(list_g[i])
    print("   ", i + 1, "학기", "%5.2f" % C)

file.close()  # 할일이 끝났으므로 파일을 닫는다