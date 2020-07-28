#엘텍공과대학 사이버보안학과
#1871063 김서영



#배열의 합계 구하는 함수
def SUM(list):
    sum = 0        #합계 변수 초기화
    for i in list: #합계 구하기
        sum += i
    return sum     #합계 반환

#배열 속 숫자들의 평균 구하는 함수
def AVERAGE(list):
    return SUM(list)/len(list)  #평균 반환
    
#빈 배열 정의
numbers=[]

#무한루프 반복
while True:
    num = int(input("양의 정수를 입력하시오.<종료는 0입력>: ")) #사용자에게 양의 정수를 입력받는다
    if num == 0:break    #0입력시 무한루프 탈출, 입력받기 종료
    elif num<0: continue #양의 정수가 아닌 음의 정수 입력 시 다시 물어본다
    numbers.append(num)  #0이 아닌 num들을 빈 배열에 추가한다

#결과값 출력
print("\n개수:%d\n합:%d\n평균:%.2f\n" %(len(numbers),SUM(numbers), AVERAGE(numbers)))
