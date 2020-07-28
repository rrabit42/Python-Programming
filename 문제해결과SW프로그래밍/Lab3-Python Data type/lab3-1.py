print("="*50)
print("     이화여자대학교 엘텍공과대학 소프트웨어학부")
print("               18학번 김서영")
print("="*50)

#변수 a,b에 각각 5,7을 할당한다.
a = 5;
b = 7;

#변수 a,b의 곱셈 한 값을 result에 저장한다.
result = a*b


#결과 화면을 출력한다.
print("***(1)곱셈***")
print("result는 %d입니다."%result)
print()
print()


print("***(2)분과 초 계산***")

#초의 값이 1000일 때, 분과 초를 계산하자
sec = 1000

 #분
min = sec//60
 #초
sec = 1000%60

#결과 화면을 출력한다.
print("%d분 %d초"%(min,sec))
