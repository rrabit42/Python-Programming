month = int(input("달을 입력하시오: "))
if 1 <= month <= 12 :
    if month % 2 == 0 :
        print("짝수달입니다.")
    else :
        print("홀수달 입니다.")
else :
    print("1과 12 사이의 숫자를 입력하시오.")

