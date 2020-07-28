while True:
    x = int(input("숫자1:  "))
    if x <= 0 :
        print("안녕")
        break
    else :
        y = int(input("숫자2:  "))
        k = int(input("어떤 배수를 찾는가?  "))

        # x 가 k의 배수가 되도록 세팅한다.
        if x % k != 0 :
            x = (x + k) // k * k

        for i in range (x, y+1, k) :
            print(i)