from tkinter import *

window = Tk()   # 윈도우 생성
button1 = Button(window, text="클릭")  # 클릭할 때 일을 하지 않는 버튼
button1.pack()

label1 = Label(window, text="0")          # 레이블 1개 생성하여 0으로 초기화
label1.pack()

def increment () :                              # label1 의 값을 0, 1, 2, 3, 으로 증가시키는 함수
    value = int(label1['text'])
    value += 1
    label1['text'] = str(value)
                                                    # label1의 값을 증가시키는 버튼
button2 = Button(window, text="증가", command=increment)  
button2.pack()

window.mainloop( )    # 윈도우가 화면에 계속 보이게 함

