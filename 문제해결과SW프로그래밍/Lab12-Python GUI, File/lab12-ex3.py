from tkinter import *

def process2():
    button['bg']='yellow'
    button['fg']='red'
    button['text']='클릭하세요!'
    button['command']=process

def process():
    button['bg']='blue'
    button['fg']='white'
    button['text']='click me!'
    button['command']=process2

window = Tk()

button = Button(window, text = '클릭하세요!', bg='yellow',fg = 'red', command=process)
button.pack()

window.mainloop()
