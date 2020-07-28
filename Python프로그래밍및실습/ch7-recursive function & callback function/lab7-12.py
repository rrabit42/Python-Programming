def findName(sentence, name) :
    found = False
    length = len(name)
    for i in range(len(sentence) - len(name)+1) :
        if sentence[i:i+length] == name :
            return True
    return False  

s = "하이, 오랜만이예요. 김이화"
if findName(s, "김이화") :
    print("있습니다")
else :
    print("없습니다")
