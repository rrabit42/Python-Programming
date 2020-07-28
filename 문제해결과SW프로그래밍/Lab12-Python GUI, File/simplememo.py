def writeMemo():
    f = open("mymemo.txt",'w')
    memo = input("한줄 메모를 입력하세요=>")
    f.write(memo+'\n')
    f.close()

def readMemo():
    f = open("mymemo.txt","r")
    memo = f.read()
    print(memo)
    f.close()

def appendMemo():
    f = open('mymemo.txt','a')
    memo = input("추가 메모를 입력하세요=>")
    f.write(memo+'\n')
    f.close()

while True:
    print("1.메모쓰기 2.메모읽기 3.메모추가 4.끝내기")
    memu = int(input("번호 선택 =>"))
    print()

    if memu == 1:writeMemo()
    elif memu == 2: readMemo()
    elif memu == 3: appendMemo()
    elif memu == 4: break

    print()
