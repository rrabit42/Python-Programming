from tkinter import *

def compute() :
    choice = var.get()
    if choice == 1 :
        F = float(e1.get())  # e1.get( ) : 현재 e1에 쓰여진 값을 읽어 온다.
        C = (F-32)*5/9      # 온도 계산
        e2.delete(0, END)
        e2.insert(0, str(C))   # e1에 C(섭씨 온도)  값을 스트링으로 변환하여 쓴다.
    elif choice == 2 :
        C = float(e2.get())
        F = C*9/5+32
        e1.delete(0, END)
        e1.insert(0, str(F))

def initialize() :
    e1.delete(0, END)
    e2.delete(0, END)
    
window = Tk()

l1 = Label(window, text="화씨")
l2 = Label(window, text="섭씨")
l1.grid(row=0, column=0)
l2.grid(row=1, column=0)

e1 = Entry(window) 
e2 = Entry(window)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

var = IntVar()  # var 는 정수를 저장할 tkinter 변수
R1 = Radiobutton(window, text="화씨->섭씨", variable=var, value=1)
R1.grid(row=2, column=0)           # R1을 클릭하면 정수 변수 var = 1이 됨

R2 = Radiobutton(window, text="섭씨->화씨", variable=var, value=2)
R2.grid(row=2, column=1)            # R2를 클릭하면 정수 변수 var = 2이 됨

b1 = Button (window, text="계산", command = compute)
b2 = Button (window, text="초기화", command = initialize)
b1.grid(row=3, column=0)
b2.grid(row=3, column=1)

window.mainloop()
