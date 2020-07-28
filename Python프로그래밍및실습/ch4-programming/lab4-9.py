x = int(input("양수 입력: "))
if x % 7 == 0 :
    print(x)
else :
    x = (x + 7) // 7 * 7
    print(x)
