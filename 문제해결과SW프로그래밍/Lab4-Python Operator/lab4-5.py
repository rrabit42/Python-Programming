#이화여자대학교 엘텍공과대학 소프트웨어학부
#1871063 김서영


#사용자로부터 Sentence를 입력받는다.
sentence = input("Sentence: ")

#Box 안에서 결과를 출력하기 위한 변수들을 지정한다.

 #화면의 길이는 80(고정)
screen_width = 80

 #Sentence의 길이
text_width = len(sentence)

 #Box의 길이
box_width = text_width+6

 #Box와 Sentence를 중앙에 위치 시키기 위한 변수
   #화면의 여백 크기
left_margin = (screen_width - box_width) //2

   #박스 안 여백 크기
box_margin = (box_width - text_width)//2



#결과 출력
print()
print(' '*left_margin + '+' + '-'*(box_width-2)    + '+')                                #BOX의 맨 위
print(' '*left_margin + 'l' + ' '*(box_width-2)    + 'l')
print(' '*left_margin + 'l' + ' '*(box_margin-1) +sentence + ' '*(box_margin-1) + 'l')
print(' '*left_margin + 'l' + ' '*(box_width-2)    + 'l')
print(' '*left_margin + '+' + '-'*(box_width-2)    + '+')
print()


