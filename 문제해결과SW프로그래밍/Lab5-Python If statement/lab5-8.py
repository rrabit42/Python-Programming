#이화여대 소프트웨어학부 사이버보안학과
#1871063 김서영



#사용자에게 정보 입력 받기
num = input("전화번호를 입력하시오: ")


#지역번호 3자리 추출하기
area = num[0:3]


#지역번호가 2자리인 경우, 번호만 추출
if area[2] == '-':
    area = num[0:2]



#지역번호를 이용해 지역 판단하기/결과 출력
if area == '02':
    print("지역번호 %s는 서울 지역 입니다." %area)
elif area == '051':
    print("지역번호 %s는 부산 지역 입니다." %area)
elif area == '053' :
    print("지역번호 %s는 대구 지역 입니다." %area)
elif area == '032' :
    print("지역번호 %s는 인천 지역 입니다." %area)
elif area == '062' :
    print("지역번호 %s는 광주 지역 입니다." %area)
else:
    print("지역번호 %s는 모르는 지역 입니다." %area)
