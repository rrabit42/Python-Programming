from tkinter import *

board = [' ']*9
gameCount = 1

def reset():
    board = [' ']*9
    gameCount = 1

def checkWin():
    if (board[0] == board[1] and board[1] == board[2] and board[0] !=' '):
        return 2
    elif (board[3] == board[4] and board[4] == board[5] and board[3] != ' '):
        return 2
    elif (board[6] == board[7] and board[7] == board[8] and board[6] != ' '):
        return 2
    elif (board[0] == board[3] and board[3] == board[6] and board[6] != ' '):
        return 2
    elif (board[1] == board[4] and board[4] == board[7] and board[1] != ' '):
        return 2
    elif (board[2] == board[5] and board[5] == board[8] and board[2] != ' '):
        return 2
    elif (board[0] == board[4] and board[4] == board[8] and board[4] != ' '):
        return 2
    elif (board[2] == board[4] and board[4] == board[6] and board[4] != ' '):
        return 2
    elif (board[0] !=' ' and board[1] != ' ' and board[2] !=' ' and board[3] !=' ' and board[4] !=' ' and board[5] !=' ' and board[6] !=' ' and board[7] !=' ' and board[8] !=' '):
        return 1
    else:
        return 0

def buttonClick(b,i):
    global gameCount
    global board

    if gameCount %2 ==1: mark = 'X'
    else: mark = '0'

    b['text']=mark
    board[i]=mark
    b['state']=DISABLED

    win = checkWin()

    if win>0:
        lbl2['fg'] = 'red'
        if win==2 and gameCount %2 ==1:
            lbl2['text'] = '*** 선수1 승리 ***'
        elif win==2:
            lbl2['text'] = '*** 선수2 승리 ***'
        else:
            lbl2['text'] = '*** 무승부 ***'
    else:
        gameCount +=1
        if gameCount %2 ==1:
            lbl2['text'] = '선수1 차례(X)'
        else:
            lbl2['text'] = '선수2 차례(O)'

def b0_click():
    buttonClick(b0,0)
    
def b1_click():
    buttonClick(b1,1)
    
def b2_click():
    buttonClick(b2,2)
    
def b3_click():
    buttonClick(b3,3)
    
def b4_click():
    buttonClick(b4,4)
    
def b5_click():
    buttonClick(b5,5)
    
def b6_click():
    buttonClick(b6,6)
    
def b7_click():
    buttonClick(b7,7)

def b8_click():
    buttonClick(b8,8)


window = Tk()
window.title("My Game")

lbl1 = Label(window, text="Tic-Tac-Toe 게임", bg='yellow', width = 35, height=2)
lbl2 = Label(window, text="선수1 차례(X)", bg = 'light grey', width=35, height=2)
lbl1.grid(row=0,column=0,columnspan=3)
lbl2.grid(row=1,column=0,columnspan=3)

w=10
h=4

b0 = Button(window, text="", width=w,height=h, command=b0_click)
b1 = Button(window, text="", width=w,height=h, command=b1_click)
b2 = Button(window, text="", width=w,height=h, command=b2_click)
b3 = Button(window, text="", width=w,height=h, command=b3_click)
b4 = Button(window, text="", width=w,height=h, command=b4_click)
b5 = Button(window, text="", width=w,height=h, command=b5_click)
b6 = Button(window, text="", width=w,height=h, command=b6_click)
b7 = Button(window, text="", width=w,height=h, command=b7_click)
b8 = Button(window, text="", width=w,height=h, command=b8_click)

b0.grid(row=2, column=0)
b1.grid(row=2, column=1)
b2.grid(row=2, column=2)
b3.grid(row=3, column=0)
b4.grid(row=3, column=1)
b5.grid(row=3, column=2)
b6.grid(row=4, column=0)
b7.grid(row=4, column=1)
b8.grid(row=4, column=2)

lbl3 = Button(window, text="김서영 제작", bg='light grey', width=35, height=2, command=reset)
lbl3.grid(row=5,column=0, columnspan=3)

window.mainloop()

