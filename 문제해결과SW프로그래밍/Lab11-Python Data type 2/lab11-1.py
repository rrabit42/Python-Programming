#엘텍공과대학 사이버보안학과
#1871063 김서영



#빈 배열 정의
numbers=[]

#무한루프 반복
while True:
    num = int(input("양의 정수를 입력하시오.<종료는 0입력>: ")) #사용자에게 양의 정수를 입력받는다
    if num == 0:break    #0입력시 무한루프 탈출, 입력받기 종료
    elif num<0: continue #양의 정수가 아닌 음의 정수 입력 시 다시 물어본다
    numbers.append(num)  #0이 아닌 num들을 빈 배열에 추가한다

count = len(numbers)     #배열에 있는 숫자의 개수 센다
sum = 0                  #합계 구할 변수 초기화

for i in numbers:        #배열에 있는 숫자의 합계 구하기
    sum += i

#개수, 합, 평균 출력
print("개수:%d\n합:%d\n평균:%0.2f"%(count,sum,sum/count))




'''
합계구하기 다른방법

for i in range(len(number)): sum += number[i]
'''
