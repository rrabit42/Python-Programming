from tkinter import *

def FtoC() :
    F = float(e1.get())  # e1.get( ) : 현재 e1에 쓰여진 값을 읽어 온다.
    C = (F-32)*5/9      # 온도 계산
    result = "%5.2f" %C
    e2.delete(0, END)  # 현재 값을 지움
    e2.insert(0, str(result))   # e1에 C(섭씨 온도)  값을 스트링으로 변환하여 쓴다.

def CtoF() :
    C = float(e2.get())
    F = C*9/5+32  
    result = "%5.2f" %F
    e1.delete(0, END)
    e1.insert(0, str(result))

def initialize() :
    e1.delete(0, END)
    e2.delete(0, END)
    
window = Tk()
window.title("온도변환기")  # 윈도우 상단 제목

l1 = Label(window, text="화씨")
l2 = Label(window, text="섭씨")
l1.grid(row=0, column=0)
l2.grid(row=1, column=0)

e1 = Entry(window) 
e2 = Entry(window)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

b1 = Button (window, text="화씨->섭씨", command = FtoC)
b2 = Button (window, text="섭씨->화씨", command = CtoF)
b3 = Button (window, text="초기화", command = initialize)
b1.grid(row=2, column=0)
b2.grid(row=2, column=1)
b3.grid(row=2, column=2)

window.mainloop()

