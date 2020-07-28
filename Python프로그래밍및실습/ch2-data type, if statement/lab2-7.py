# 과목리스트


subjects = ['국어', '영어', '수학', '물리']
print(subjects)      # 리스트 출력
print(subjects[0])   # 국어 출력 (문자열 1개)
print()

# 한과목씩 추가
subjects.append('화학')
subjects.append('생물')

# 모든 과목 출력
print("모든 과목 = ", subjects)
print()

# 모든 과목의 첫 글자 출력
print(subjects[0][0])
print(subjects[1][0])
print(subjects[2][0])
print(subjects[3][0])
print(subjects[4][0])
print(subjects[5][0])
print()

# 한 줄에 3과목씩 출력
print(subjects[0][0], end = ", ")
print(subjects[1][0], end = ", ")
print(subjects[2][0])
print(subjects[3][0], end = ", ")
print(subjects[4][0], end = ", ")
print(subjects[5][0])





