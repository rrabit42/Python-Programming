#김서영(1871063)

print("*"*30)

#사용자에게서 원하는 정보 입력 받기
name = input("학생 이름은? ")
korean = int(input("국어 점수는? "))
english = int(input("영어 점수는? "))
math = int(input("수학 점수는? "))


#총점 구하기

sum = korean + english + math

#평균 구하기

average = sum/3


#결과 출력하기

print()
print("="*30)
print(name,"총점과 평균입니다.")
print("총점 = ",sum,"점")
print("평균 = ",average,"점")
