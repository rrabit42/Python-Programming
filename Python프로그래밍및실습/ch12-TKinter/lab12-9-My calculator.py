from tkinter import *

# button 0, 1, 2, ... , 9를 눌렀을 때 실행할 함수들 정의

def btn0Compute():
    choice = var.get()  # radio button  값 받음
    
    if choice == 1:  # 숫자1 입력 상태
        e1Val = e1.get()
        if e1Val == "" :   # 비어 있다면
            newNum = 0  # 새로운 값은 0이다
        else:                  # 비어 있지 않다면
            oldNum = int(e1Val)   # 그 값을 숫자로 변환 
            newNum = oldNum * 10 + 0   # 새로운 숫자를 계산한다
        e1.delete(0, END)     # 숫자1에 써 있던 값을 지운다
        e1.insert(0, str(newNum))  # 새로 계산된 숫자를 적어 넣는다
        
    elif choice == 2:   # 숫자2 입력 상태
        e2Val = e2.get()
        if e2Val == "" :   # 비어 있다면
            newNum = 0   # 새로운 값은 0이다
        else:    # 비어 있지 않다면
            oldNum = int(e2Val)   # 그 값을 숫자로 변환
            newNum = oldNum * 10 + 0  # 새로운 숫자를 계산한다
        e2.delete(0, END)      # 숫자2에 써 있던 값을 지운다
        e2.insert(0, str(newNum))  # 새로 계산된 숫자를 적어 넣는다

def btn1Compute():
    choice = var.get()  
    
    if choice == 1:  # 숫자1 입력 상태
        e1Val = e1.get()
        if e1Val == "" :   
            newNum = 1  
        else:                  
            oldNum = int(e1Val)   
            newNum = oldNum * 10 + 1   # 곱하기 10 더하기 1
        e1.delete(0, END)     
        e1.insert(0, str(newNum))  
        
    elif choice == 2:   # 숫자2 입력 상태
        e2Val = e2.get()
        if e2Val == "" :   
            newNum = 1  
        else:    
            oldNum = int(e2Val)   
            newNum = oldNum * 10 + 1  # 곱하기 10 더하기 1
        e2.delete(0, END)      
        e2.insert(0, str(newNum))  

def btn2Compute():
    choice = var.get()  
    
    if choice == 1:  # 숫자1 입력 상태
        e1Val = e1.get()
        if e1Val == "" :   
            newNum = 2  
        else:                  
            oldNum = int(e1Val)   
            newNum = oldNum * 10 + 2   # 곱하기 10 더하기 2
        e1.delete(0, END)     
        e1.insert(0, str(newNum))  
        
    elif choice == 2:   # 숫자2 입력 상태
        e2Val = e2.get()
        if e2Val == "" :   
            newNum = 2  
        else:    
            oldNum = int(e2Val)   
            newNum = oldNum * 10 + 2  # 곱하기 10 더하기 2
        e2.delete(0, END)      
        e2.insert(0, str(newNum))  

def btn3Compute():
    choice = var.get()  
    
    if choice == 1:  # 숫자1 입력 상태
        e1Val = e1.get()
        if e1Val == "" :   
            newNum = 3  
        else:                  
            oldNum = int(e1Val)   
            newNum = oldNum * 10 + 3   # 곱하기 10 더하기 3
        e1.delete(0, END)     
        e1.insert(0, str(newNum))  
        
    elif choice == 2:   # 숫자2 입력 상태
        e2Val = e2.get()
        if e2Val == "" :   
            newNum = 3  
        else:    
            oldNum = int(e2Val)   
            newNum = oldNum * 10 + 3  # 곱하기 10 더하기 3
        e2.delete(0, END)      
        e2.insert(0, str(newNum))  

def btn4Compute():
    choice = var.get()  
    
    if choice == 1:  # 숫자1 입력 상태
        e1Val = e1.get()
        if e1Val == "" :   
            newNum = 4  
        else:                  
            oldNum = int(e1Val)   
            newNum = oldNum * 10 + 4   # 곱하기 10 더하기 4
        e1.delete(0, END)     
        e1.insert(0, str(newNum))  
        
    elif choice == 2:   # 숫자2 입력 상태
        e2Val = e2.get()
        if e2Val == "" :   
            newNum = 4  
        else:    
            oldNum = int(e2Val)   
            newNum = oldNum * 10 + 4  # 곱하기 10 더하기 4
        e2.delete(0, END)      
        e2.insert(0, str(newNum))  

def btn5Compute():
    choice = var.get()  
    
    if choice == 1:  # 숫자1 입력 상태
        e1Val = e1.get()
        if e1Val == "" :   
            newNum = 5  
        else:                  
            oldNum = int(e1Val)   
            newNum = oldNum * 10 + 5  # 곱하기 10 더하기 5
        e1.delete(0, END)     
        e1.insert(0, str(newNum))  
        
    elif choice == 2:   # 숫자2 입력 상태
        e2Val = e2.get()
        if e2Val == "" :   
            newNum = 5  
        else:    
            oldNum = int(e2Val)   
            newNum = oldNum * 10 + 5  # 곱하기 10 더하기 5
        e2.delete(0, END)      
        e2.insert(0, str(newNum))  

def btn6Compute():
    choice = var.get()  
    
    if choice == 1:  # 숫자1 입력 상태
        e1Val = e1.get()
        if e1Val == "" :   
            newNum = 6  
        else:                  
            oldNum = int(e1Val)   
            newNum = oldNum * 10 + 6   # 곱하기 10 더하기 6
        e1.delete(0, END)     
        e1.insert(0, str(newNum))  
        
    elif choice == 2:   # 숫자2 입력 상태
        e2Val = e2.get()
        if e2Val == "" :   
            newNum = 6 
        else:    
            oldNum = int(e2Val)   
            newNum = oldNum * 10 + 6  # 곱하기 10 더하기 6
        e2.delete(0, END)      
        e2.insert(0, str(newNum))  

def btn7Compute():
    choice = var.get()  
    
    if choice == 1:  # 숫자1 입력 상태
        e1Val = e1.get()
        if e1Val == "" :   
            newNum = 7  
        else:                  
            oldNum = int(e1Val)   
            newNum = oldNum * 10 + 7   # 곱하기 10 더하기 7
        e1.delete(0, END)     
        e1.insert(0, str(newNum))  
        
    elif choice == 2:   # 숫자2 입력 상태
        e2Val = e2.get()
        if e2Val == "" :   
            newNum = 7 
        else:    
            oldNum = int(e2Val)   
            newNum = oldNum * 10 + 7  # 곱하기 10 더하기 7
        e2.delete(0, END)      
        e2.insert(0, str(newNum))  

def btn8Compute():
    choice = var.get()  
    
    if choice == 1:  # 숫자1 입력 상태
        e1Val = e1.get()
        if e1Val == "" :   
            newNum = 8  
        else:                  
            oldNum = int(e1Val)   
            newNum = oldNum * 10 + 8   # 곱하기 10 더하기 8
        e1.delete(0, END)     
        e1.insert(0, str(newNum))  
        
    elif choice == 2:   # 숫자2 입력 상태
        e2Val = e2.get()
        if e2Val == "" :   
            newNum = 8 
        else:    
            oldNum = int(e2Val)   
            newNum = oldNum * 10 + 8  # 곱하기 10 더하기 8
        e2.delete(0, END)      
        e2.insert(0, str(newNum))  

def btn9Compute():
    choice = var.get()  
    
    if choice == 1:  # 숫자1 입력 상태
        e1Val = e1.get()
        if e1Val == "" :   
            newNum = 9 
        else:                  
            oldNum = int(e1Val)   
            newNum = oldNum * 10 + 9   # 곱하기 10 더하기 9
        e1.delete(0, END)     
        e1.insert(0, str(newNum))  
        
    elif choice == 2:   # 숫자2 입력 상태
        e2Val = e2.get()
        if e2Val == "" :   
            newNum = 9 
        else:    
            oldNum = int(e2Val)   
            newNum = oldNum * 10 + 9  # 곱하기 10 더하기 9
        e2.delete(0, END)      
        e2.insert(0, str(newNum))  

# 초기화  button 실행 함수

def initialize():
    e1.delete(0, END)
    e2.delete(0, END)
    e3.delete(0, END)

#  덧셈 button 실행 함수

def add():
    e1Val = e1.get()
    e2Val = e2.get()
    if e1Val == "" :  # 비어 있으면 0이라고 가정하자
        op1 = 0
    else:
        op1 = int(e1Val)

    if e2Val == "" :  # 비어 있으면 0이라고 가정하자
        op2 = 0
    else:
        op2 = int(e2Val)

    result = op1 + op2
    e3.delete(0, END)
    e3.insert(0, str(result))   

# 계산기 만들기 시작~

window = Tk()
window.title("나의 계산기")

# frame 정의

frame1 = Frame(window)   # 숫자1, 숫자2, 결과 label과 entry 가 놓일 곳
frame2 = Frame(window)   # radio button 들이 있는 곳
frame3 = Frame(window)   # 0, 1, 2, ... , 9 button 들이 있는 곳
frame4 = Frame(window)   # 덧셈, 초기화 button 있는 곳

frame1.pack()
frame2.pack()
frame3.pack()
frame4.pack()

# 숫자1, 숫자2, 결과 label, entry 정의

l1 = Label(frame1, text="숫자1")
l2 = Label(frame1, text="숫자2")
l3 = Label(frame1, text="결과")
e1 = Entry(frame1) 
e2 = Entry(frame1)
e3 = Entry(frame1)

# 숫자1, 숫자2, 결과 label, entry의 frame1 안에서의 위치를 정한다

l1.grid(row=0, column=0)
l2.grid(row=1, column=0)
l3.grid(row=2, column=0)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)

# radio button 2개를 frame2안에 둔다

var = IntVar()  # var 는 정수를 저장할 tkinter 변수
R1 = Radiobutton(frame2, text="숫자1 입력", variable=var, value=1)
R1.grid(row=0, column=0)           # R1을 클릭하면 정수 변수 var = 1이 됨

R2 = Radiobutton(frame2, text="숫자2 입력", variable=var, value=2)
R2.grid(row=0, column=1)            # R2를 클릭하면 정수 변수 var = 2이 됨

# frame3에 있는 0, 1, 2, ... , 9 button 들의 정의

btn0 = Button (frame3, text="0", command = btn0Compute)
btn1 = Button (frame3, text="1", command = btn1Compute)
btn2 = Button (frame3, text="2", command = btn2Compute)
btn3 = Button (frame3, text="3", command = btn3Compute)
btn4 = Button (frame3, text="4", command = btn4Compute)
btn5 = Button (frame3, text="5", command = btn5Compute)
btn6 = Button (frame3, text="6", command = btn6Compute)
btn7 = Button (frame3, text="7", command = btn7Compute)
btn8 = Button (frame3, text="8", command = btn8Compute)
btn9 = Button (frame3, text="9", command = btn9Compute)

# frame4에 있는 덧셈, 초기화 button 들의 정의

btnAdd = Button (frame4, text="덧셈(+)", command = add)
btnInit = Button (frame4, text="초기화", command = initialize)

#  frame3, frame4 안에 있는 button 들의 위치 설정

btn0.grid(row=0, column=0)
btn1.grid(row=0, column=1)
btn2.grid(row=0, column=2)
btn3.grid(row=0, column=3)
btn4.grid(row=0, column=4)
btn5.grid(row=1, column=0)
btn6.grid(row=1, column=1)
btn7.grid(row=1, column=2)
btn8.grid(row=1, column=3)
btn9.grid(row=1, column=4)
btnAdd.pack(side=LEFT)
btnInit.pack(side=RIGHT)

window.mainloop()
