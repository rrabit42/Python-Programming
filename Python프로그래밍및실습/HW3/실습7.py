s = [['박기선', [70, 80, 90], [60, 70, 80, 85, 90], [90, 80]],
     ['안채은', [70, 80, 60, 80], [70, 50, 60], [100, 90, 80, 60, 70]],
     ['김나연', [90, 80, 90], [70, 90], [80, 60, 70, 50], [90, 90, 80]]]

name = input("학생 이름: ")  # 학생 이름을 물어본다

for i in range(len(s)):  # 리스트 안에 있는 리스트를 탐색하는데
    if name == s[i][0]:  # 입력한 이름이랑 속에 있는 리스트의 이름이 같으면
        print(name)  # 이름을 출력하고
        del s[i][0]  # 용이한 출력을 위해 이름은 리스트에서 삭제
        n = len(s[i])  # 리스트 길이 변수 지정
        for j in range(n):  # 학기마다 점수출력을 위한 for구문
            print(j + 1, "학기:", s[i][j])  # 그 i리스트의 있는 리스트를 j(리스트의 끝까지) 반복하여 점수출력

