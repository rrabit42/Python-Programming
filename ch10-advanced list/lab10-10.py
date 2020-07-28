S = [["이하경", 80, 70, 90], ["김윤아", 80, 75, 90], ["현오주", 80, 80, 80],
            ["석지원", 70, 100, 80], ["김혜진", 100, 80, 85], ["이재은", 80, 80, 70]]


s1 = []
s1.append(input("이름 : "))
s1.append(int(input("점수1: ")))
s1.append(int(input("점수2: ")))
s1.append(int(input("점수3: ")))

S.append(s1)
S.sort()  # 사전 순서 정렬, 즉 이름순이 될 것임

for i in range (len(S)) :
  print (S[i])
