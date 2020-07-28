#이화여자대학교 엘텍공과대학 소프트웨어학부
#1871063 김서영



#사용자에게 정보를 입력받는다

name = input("이름을 입력하시오: ")             #이름
birth = input("주민등록번호를 입력하시오: ")    #주민등록번호



#생년월일을 슬라이싱 한다

year = "19"+ birth[0:2]    #년도
month = birth[2:4]         #월
day = birth[4:6]           #일


#주민등록번호로 성별을 구분하는 조건문
if birth[8] == 1:
    gender = "남성"
else :
    gender = "여성"


#결과화면 출력
print()
print("%s 고객의 생년월일은\n%s년 %s월 %s일입니다." %(name,year,month,day))
print()
print("%s 고객은 %s입니다." %(name,gender))
