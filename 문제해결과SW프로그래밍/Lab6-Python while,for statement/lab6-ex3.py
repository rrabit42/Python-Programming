year = int(input("연도 입력하세요:"))

while(year<1900 or year>2020):
    year = int(input("연도 입력하세요:"))

if (year%400==0 or(year%4==0 and year%10!=0)):
    print("윤년이다!!!")
else:
    print("윤년 아니다!")
