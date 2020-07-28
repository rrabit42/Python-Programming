import turtle
t = turtle.Turtle()

print("다양한 크기의 별을 그려 드립니다.")
print("선의 굵기와 길이를 입력해 주세요.")
width = int(input("선의 굵기 (5~20): "))
length = int(input("선의 길이 (100~150): "))            

t.width(width)
t.color("green")

t.forward(length)
t.left(144)
t.forward(length)
t.left(144)
t.forward(length)
t.left(144)
t.forward(length)
t.left(144)
t.forward(length)

print("=" * 30)
print("다 그렸어요!")
