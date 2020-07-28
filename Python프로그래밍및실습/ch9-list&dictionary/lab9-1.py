numbers = []

while True:
    n = int(input("숫자: "))
    if n == 0 :
        break
    else :
        numbers.append(n)
print(len(numbers))  # 개수

sum = 0
for i in numbers :
    sum += i
print(sum)  # 합계

average = sum / len(numbers)
print(average)  # 평균

