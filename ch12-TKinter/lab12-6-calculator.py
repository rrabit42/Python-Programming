from tkinter import *

def btnClear() :
    e1.delete(0, END)
    e2.delete(0, END)
    result.delete(0, END)
    
def btnPlus() :
    a = float(e1.get())
    b = float(e2.get())
    r = a + b
    result.delete(0, END)
    result.insert(0, str(r))

def btnMinus() :
    a = float(e1.get())
    b = float(e2.get())
    r = a - b
    result.delete(0, END)
    result.insert(0, str(r))

def btnMultiply() :
    a = float(e1.get())
    b = float(e2.get())
    r = a * b
    result.delete(0, END)
    result.insert(0, str(r))

def btnDivide() :
    a = float(e1.get())
    b = float(e2.get())
    r = a / b
    r2 = "5.2f" %r
    result.delete(0, END)
    result.insert(0, str(r2))
    
window = Tk()

l1 = Label(window, text = "숫자1")
l2 = Label(window, text = "숫자2")
l3 = Label(window, text = "결과값")
l1.grid(row=0, column=0)
l2.grid(row=1, column=0)
l3.grid(row=2, column=0)

e1 = Entry(window,) 
e2 = Entry(window)
result = Entry(window)
e1.grid(row=0, column=1, columnspan=4)
e2.grid(row=1, column=1, columnspan=4)
result.grid(row=2, column=1, columnspan=4)

btnClear = Button (window, text="초기화", width=5, command = btnClear)
btnPlus = Button (window, text="+", width=5, command = btnPlus)
btnMinus = Button (window, text="-", width=5, command = btnMinus)
btnMultiply = Button (window, text="*", width=5, command = btnMultiply)
btnDivide = Button (window, text="/", width=5, command = btnDivide)

btnPlus.grid(row=3,column=0)
btnMinus.grid(row=3,column=1)
btnMultiply.grid(row=3,column=2)
btnDivide.grid(row=3,column=3)
btnClear.grid(row=3,column=4)

window.mainloop()

