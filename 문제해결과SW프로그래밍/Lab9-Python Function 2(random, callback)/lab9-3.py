def getGrade(n):
    if n>=90:
        return 'A'
    elif n>=80:
        return 'B'
    elif n>=70:
        return 'C'
    elif n>=60:
        return 'D'
    else:
        return 'F'


score = int(input("점수를 입력하시오: "))

while score<0 or score>100:
    print("잘못입력하셨습니다.\n")
    score = int(input("점수를 입력하시오: "))

grade = getGrade(score)
print("성적은 %s입니다." %grade)
