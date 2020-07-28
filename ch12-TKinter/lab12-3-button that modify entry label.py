from tkinter import *

window = Tk()   # 윈도우 생성

e1 = Entry(window)   # 값을 입출력할 수 있는 곳
e1.pack()                 # e1을 적당하게 배치시킴
e1.insert(0, "0")

def increment () :                              # label1 의 값을 0, 1, 2, 3, 으로 증가시키는 함수
    value = int(e1.get())
    value += 1
    e1.delete(0, END)                         # 현재 보이는 값을 지움
    e1.insert(0, str(value))                    # 계산한 값을 e1 에 보이도록 함
                                                    # e1의 값을 증가시키는 버튼
button = Button(window, text="증가", command=increment)  
button.pack()

window.mainloop( )    # 윈도우가 화면에 계속 보이게 함

