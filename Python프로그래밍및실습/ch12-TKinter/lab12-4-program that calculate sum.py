from tkinter import *

def add():
    a = int(e1.get())
    s = int(sum['text'])
    s += a
    sum['text'] = str(s)
    e1.delete(0, END)
    
window = Tk()

sum = Label(window)
sum.grid(row=0, column=1)
sum['text'] = 0

l1 = Label(window, text="현재 합계:")
l1.grid(row=0, column=0)

e1 = Entry(window)
e1.grid(row=1, column=0, columnspan=2)

b1 = Button(window, text="더하기(+)", command=add)
b1.grid(row=2, column=0)

b2 = Button(window, text="종료", command=window.destroy)
b2.grid(row=2, column=1)

window.mainloop()
