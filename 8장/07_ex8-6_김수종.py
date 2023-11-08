'''
    작성일 : 2023년 11월 8일
    작성자 : 컴퓨터공학부 2202395007 김수종
    설명 : 심화문제 8-3
    1. 학번, 이름, 번화번호의 3쌍의 요소를 가지는
       student_tuple이라는 튜플이 존재한다.
    
    2. 이 튜플을 수정하여{학변 : 이름}의 쌍으로
       이루어진 딕셔너리를 만들어 출력
    
    3. 이 정보를 이용하여 학생의 학번으로 조회할 경우
       학번, 이름과 전화번호가 출력되게 하기
'''

# 학생 정보 튜플 작성
student_tuple = [("211101", "강이안", "010-123-1111"), ("211102", "박동민", "010-123-2222"), ("211103", "김수정", "010-123-3333")]
student_dict = {} # 비어있는 딕셔너리 생성

# 딕셔너리 추가
for id, name, number in student_tuple :
    student_dict[id] = name # 학번에 맞는 이름 저장
    
# 딕셔너리 출력
for key, value in student_dict.items() :
    print(key,":",value) 
    
# 학번 입력 받아 이름과 연락처 출력
number = input("학번을 입력하세요 : ") # 학번 입력 받기
for num in student_tuple : # 튜플 갯수 만큼 반복
    if number == num[0]: # 해당 학번이 포함된 튜플이면
        phone_num = num[2] # 해당 학번의 전화번호 저장

# 결과 출력
print(f"{number} 학생은 {student_dict[number]}이며, 전화번호는 {phone_num}입니다.")
