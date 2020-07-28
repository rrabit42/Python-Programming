def computeSum(numbers) :
    sum = 0
    for i in range(len(numbers)) :
        sum += numbers[i]
    return sum

def computeAvg(numbers) :
    sum = 0
    for i in range(len(numbers)) :
        sum += numbers[i]
    average = sum / len(numbers)
    return average

numbers = []
while True:
    n = int(input("숫자: "))
    if n == 0 :
        break
    else :
        numbers.append(n)

print(len(numbers))  # 개수
hap = computeSum(numbers)
avg = computeAvg(numbers)

print(hap)  # 합계
print(avg)  # 평균
