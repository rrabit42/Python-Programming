x = int(input("숫자1:  "))
y = int(input("숫자2:  "))

# x 가 7의 배수가 되도록 세팅한다.
if x % 7 != 0 :
    x = (x + 7) // 7 * 7

for i in range (x, y+1, 7) :
    print(i)