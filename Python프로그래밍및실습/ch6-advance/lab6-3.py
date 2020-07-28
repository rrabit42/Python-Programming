basket = ["사과", "귤", "바나나", "토마토", "파인애플"] 

print(basket, "있습니다.")
print()

fruit = input("무슨 과일을 드릴까요? ")
n = basket.count(fruit)
if n >= 1 :
    print("원하시는 " + fruit + "을/를 드리겠습니다!")
    print("맛있게 드세요~")
    print()
    basket.remove(fruit)
    print("남은 과일은 ", basket, " 입니다!")
else :
    print("그런 과일은 없습니다.")
    print()
    print("남은 과일은 ", basket, " 입니다!")  
