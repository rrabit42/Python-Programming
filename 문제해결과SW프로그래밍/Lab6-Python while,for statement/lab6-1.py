#이화여대 소프트웨어학부 사이버보안과
#1871063 김서영




#사용자에게 양의 정수 n을 입력 받는다
n = int(input("양의 정수:"))


#양의 정수 외의 수를 입력할 시, 양의 정수 입력할 때까지 물어보기
while(n<=0):
    n = int(input("양의 정수:"))


#변수 지정
i=1       #for문 위한 변수
sum=0     #합계 변수


#n보다 작은 수 중 3의 배수들의 합 구하기

while(i<n):                #i가 n보다 작을 경우(range때문에)
    for i in range(i,n):   #i이상 n미만의 수
        if i%3 == 0:       #3의 배수일 경우 합산하기
            sum+=i
            i+=1           #다음 수로 넘어가서 3의 배수 인지 확인
        else:
            i+=1           #3의 배수 아닐 경우 바로 다음 수로 넘어가기


#결과 값 출력
print(sum)
