'''
    작성일 : 2023년 10월 18일
    작성자 : 컴퓨터공학부 2202395007 김수종
    설명 : 리스트의 객체 생성과 참조
'''

fruits1 = ['딸기','수박','바나나']

fruits2 = fruits1

print("fruits1 :",fruits1)
print("fruits2 :",fruits2)

# 실제 값을 복사하는 것이 아니라 리스트의 저장 위치(주소)가 복사된다
fruits2[1] = '망고' # fruits2의 [1]번지 과일을 망고로 바꾸면

print("fruits1 :",fruits1) # 모두 1번지 내용이 망고로 바뀐다
print("fruits2 :",fruits2) # 주소를 참조하기 때문

# 리스트 주소 확인
print("fruits1의 ID :",id(fruits1))
print("fruits2의 ID :",id(fruits2))

'''
    리스트 내용을 복제하기 list() 함수
'''

# 내용 복제 1
fruits2 = list(fruits1)
print(":: 내용 복제 후 1 ::")
print("fruits1 :",fruits1)
print("fruits2 :",fruits2)
print("fruits1의 ID :",id(fruits1))
print("fruits2의 ID :",id(fruits2))
print()

# 내용 복제 2
fruits3 = fruits1[:]
print(":: 내용 복제 후 2 ::")
print("fruits1 :",fruits1)
print("fruits3 :",fruits3)
print("fruits1의 ID :",id(fruits1)) # id 정보가 다르다
print("fruits3의 ID :",id(fruits3))
print()

fruits3[0] = '수박'
print(":: fruits3의 0번지에 수박으로 내용을 바꾼 후 ::")
print("fruits1 :",fruits1)
print("fruits3 :",fruits3)
