week = ['일요일', '월요일', '화요일', '수요일', '목요일', '금요일', '토요일']
day = int (input("날짜를 입력하세요 : "))

if day < 1 or day > 30 :
    print("잘못 입력하셨습니다.")
else :
    i = day % 7 - 1
    print(week[i])

