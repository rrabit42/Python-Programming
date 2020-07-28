#엘텍공과대학 사이버보안학과
#1871063 김서영



dic = {}

while True:
    key = input("이름을 입력하세요: ")
    if key =="": break
    value_list=[]
    school =input("학교를 입력하세요: ")
    depart =input("학과를 입력하세요: ")
    grade =input("학년을 입력하세요: ")
    phone =input("전화번호을 입력하세요: ")
    value_list.append(school)
    value_list.append(depart)
    value_list.append(grade)
    value_list.append(phone)
    dic[key] = value_list

print("\n검색을 시작합니다.")
while (1):
    search = input("\n찾으려는 사람의 이름을 입력하세요: ")
    if search == "":
        print("안녕")
        break
    print("찾으려는 사람에 대한 정보입니다.\n")
    print(dic[search])
