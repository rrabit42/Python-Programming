from tkinter import *
window = Tk()

b= Label(window,text='Name')
b.pack()

txt = Entry(window)
txt.pack()

btn = Button(window, text='Ok')
btn.pack()

window.mainloop()
