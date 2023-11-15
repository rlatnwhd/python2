'''
    작성일 : 2023년 11월 15일
    작성자 : 컴퓨터공학부 2202395007 김수종
    설명 : LAB 9-2 : 트위터 메세지 처리의 단어 추출
           띄어쓰기로 문자열을 분리하고, 단어의 개수를 찾아라
'''

text = "There's a reason some people are working to make \
        it harder to vote, especially for people of color. \
        It’s because when we show up, things change."
        
# 띄어쓰기로 문자열을 분리하고, 단어의 개수를 찾아라
text_list = text.split() # 공백을 기준으로 분리
print(text_list) # 출력
print("word count", len(text_list)) # 분리된 문자 리스트의 개수 출력

# 도전문제 9-1
# 회사 이름은 **로 표시
# KT, Samsung, LG, SKT
text = '[ARTICLE] 200820 BLACKPINK Jennie is regarded to have great effect on KT Mystic \
        Red as it was chosen by 50% of those who prebooked for the Samsung Galaxy Note 20 ( \
        LG U+ Mystic Pink 30%, SKT Mystic Blue not disclosed) '

# 모든 문자를 소문자로 변환

# 소문자로 바뀐 단어들을 공백으로 구분한다
# 구분된 단어를 검사한다.(판단)=> 단어가 kt 또는 samsung 또는 lg 또는 skt인가?
# 검사하는 단어가 회사명이면 **으로 바꾼다.
# 아니면 그 단어는 그대로 사용한다.
text_list = text.lower().split()
for company in text_list:
    if(company=="lg" or company=="samsung" or company=="skt" or company=="kt"):
        num = text_list.index(company) # 해당 회사 인덱스 번호 저장
        text_list.remove(company) # 회사 항목 삭제
        text_list.insert(num,"**") # 삭제한 인덱스 번호 자리에 "**"을 추가
        
print(" ".join(text_list))