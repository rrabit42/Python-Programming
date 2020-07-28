fruits = ["사과", "배", "귤", "토마토", "포도"]
print(fruits)

# 끝에 삽입
fruits.append("바나나")
print(fruits)
fruits.append("파인애플")
print(fruits)

#특정 값 삭제
fruits.remove("귤")
print(fruits)

#특정 위치의 값 삭제
del fruits[1]
print(fruits)

#특정 위치에 삽입
fruits.insert(2, "자두")
print(fruits)

#특정 위치의 값 수정
fruits[0] = "부사"
print(fruits)

#특정 위치의 값 수정 (범위 지정)
fruits[0:2] = ["홍옥", "방울토마토"]
print(fruits)

#사전식 순서로 정렬
fruits.sort()
print(fruits)

#리스트에 포함되어 원소 개수를 센다
n = fruits.count("홍옥")
print(n)