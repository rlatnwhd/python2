'''
    작성일 : 2023년 11월 1일
    작성자 : 컴퓨터공학부 2202395007 김수종
    설명 : 8.1 키와 값을 갖는 딕셔너리
'''

# 빈 딕셔너리 생성
phone_book1 = {}

# 딕셔너리 값 저장, key value [key] = value
phone_book1['김수종'] = '010-1234-5678'

print('phone_book1 : ',phone_book1)

# 딕셔너리에 값 저장 2. {key : value}
phone_book2 = {'홍길동' : '010-1234-5678','김수종' : '010-1577-1588'}
print('phone_book2 : ',phone_book2)

phone_book3 = {}
phone_book3['김수종'] = '010-1234-5678'
phone_book3['홍길동'] = '010-2437-1037'
phone_book3['정뚝떨'] = '010-6926-7652'
phone_book3['이발장'] = '010-5719-3257'
phone_book3['신소재'] = '010-3246-8674'
print('phone_book3 : ',phone_book3)

# 모든 key 출력
print(phone_book3.keys())
# 모든 value 출력
print(phone_book3.values())
# 모든 key, value 출력
print(phone_book3.items())

print()
print(":: 전화번호 phone_book3 items()출력 ::")
for name, phone_num in phone_book3.items():
    print(name, ':', phone_num)
    
print()
print(":: 전화번호 phone_book3[key]로 접근하여 출력 ::")
for key in phone_book3.keys():
    print(key, ":", phone_book3[key])

print()
print(":: 딕셔너리 작성 시 :(콜론)을 기준으로 key:value 작성 ::")
person_dict = {'name' : '김수종', 'age' : 18, 'class' : '1학년'}

print("name : ",person_dict['name'])
print("age : ",person_dict['age'])
print("class : ",person_dict['calss'])

print()
print(":: 정렬 ::")
# phone_book3를 정렬
print(sorted(phone_book3)) # key를 기준으로 정렬하여 리스트로 반환
    
print()
print(":: 키를 기준으로 전체 정렬 ::")
sort_phone_book3 = sorted(phone_book3.items(), key=lambda x : x[0]) # lambda 함수(이름없는 함수)
print(sort_phone_book3)

print()
print(":: 값을 기준으로 전체 정렬 ::")
sort_phone_book3 = sorted(phone_book3.items(), key=lambda x : x[1]) # lambda 함수(이름없는 함수)
print(sort_phone_book3)

print()
print(":: 항목 삭제 ::")
del phone_book3['김수종'] # key 값을 지우면 value값도 삭제됨
print(phone_book3)

print()
print(":: 항목 전제 삭제 ::")
phone_book3.clear()
print(phone_book3)