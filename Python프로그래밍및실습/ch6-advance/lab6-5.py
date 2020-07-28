basket = ["사과", "귤", "바나나", "토마토", "파인애플"] 

print("과일을 나누어 드립니다. ")

while  len(basket) > 0 :
    print(basket[0])
    del basket[0]
    print("남은 과일은 ", basket)
