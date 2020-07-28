# 숫자들 읽고 합하기


nums = [ ]  # 빈 리스트
n = 5       # 읽으려는 숫자 개수
for i in range (n) :
    n = int(input("정수: "))
    nums.append(n)

print("\n입력하신 숫자 리스트")
print(nums)

print("\n입력하신 숫자들의 합")
print(sum(nums))#sum함수 사용!

