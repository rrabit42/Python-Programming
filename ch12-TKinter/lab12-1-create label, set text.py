from tkinter import *

window = Tk()   # 윈도우 생성

label1 = Label(window, text="안녕")   # Label 생성, 화면에는 "안녕" 이 보임
label1.pack()          # label1 을 적당하게 배치시킴

label2 = Label(window)   # Label 생성, 화면에는 아무 것도 안 보임
label2.pack()          # label2를 적당하게 배치시킴
label2['text'] = "환영"  # 화면에 "환영"이 보임, 이렇게 나중에 대입/수정이 가능

window.mainloop( )    # 윈도우가 화면에 계속 보이게 함