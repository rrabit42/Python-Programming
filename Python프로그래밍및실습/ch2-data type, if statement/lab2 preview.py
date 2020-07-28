# 리스트 복습 프로그램


import turtle
t = turtle.Turtle()
t.shape("turtle")

color_list = ["red", "yellow", "green", "blue", "purple"]
print(len(color_list))
print()

for i in range(7):    
    print(i)

print()

# python은 for 쓸 때 {} 대신 들여쓰기 맞춰주기!
for i in range(7) : 
    print(i, end = ", ")
    print(i+1, end = ", ")
    print(i+2)   



    

    
    
