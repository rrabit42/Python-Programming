dict = {}
info = []
while True:
    name = input("이름: ")
    if name != "" :
        school = input("학교: ")
        year = input("학년: ")
        phone = input("전화: ")
        info.append(school)
        info.append(year)
        info.append(phone)
        dict[name] = info
        info = []
    else :
        break

while True:
    name = input("검색할 이름: ")
    if name != "" :
        print(dict[name])
    else :
        print ("안녕")
        break
    
