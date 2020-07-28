from tkinter import *

def select():    
   label['text']= str(var.get()) + "번 선택"
   
window = Tk()
var = IntVar()  # var 는 정수를 저장할 tkinter 변수

R1 = Radiobutton(window, text="1번", variable=var, value=1, command=select)
R1.pack()           # R1을 클릭하면 정수 변수 var = 1이 됨

R2 = Radiobutton(window, text="2번", variable=var, value=2, command=select)
R2.pack()           # R2를 클릭하면 정수 변수 var = 2이 됨

R3 = Radiobutton(window, text="3번", variable=var, value=3, command=select)
R3.pack()           # R3를 클릭하면 정수 변수 var = 3이 됨

label = Label(window)
label.pack()
window.mainloop()
