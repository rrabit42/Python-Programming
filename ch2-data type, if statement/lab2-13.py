# 입력할 숫자 개수 모를 때


nums = [ ] # 비어 있는 리스트
n = int(input("입력할 숫자의 개수는 : "))

for i in range (n) :
    n = int(input("정수: "))
    nums.append(n)

print("\n입력하신 숫자 리스트")
print(nums)

print("\n입력하신 숫자들의 합")
print(sum(nums)) #sum 함수 사용!

