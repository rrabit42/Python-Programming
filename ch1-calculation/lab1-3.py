# 신입생 오리엔테이션

# 번호표 --> 방번호, 방안에서의 번호 구하기
number = int(input("번호표 : "))

room = (number-1) // 15 + 1  # 방번호
print("방번호: ", room)

numInRoom = number - (room-1) * 15  # 방안에서의 번호
print("방안에서의 번호", numInRoom)
