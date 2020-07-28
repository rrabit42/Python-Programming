basket = []   # 비어있는 바구니 생성

# 바구니에 과일 담기
while True :
   fruit = input("과일 : ")
   if fruit == "" :  # 엔터키, 즉 입력이 없다 
       print("입력하신 과일들은 다음과 같습니다.")
       print(basket)
       break
   else :
       basket.append(fruit)
	