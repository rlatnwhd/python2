'''
    작성일 : 2023년 11월 8일
    작성자 : 컴퓨터공학부 2202395007 김수종
    설명 : 심화문제 8-3
    1. 학번, 이름, 번화번호의 3쌍의 요소를 가지는
       student_tuple이라는 튜플이 존재한다.
    
    2. 이 튜플을 수정하여{학변 : [이름, 전화번호]}의 쌍으로
       이루어진 딕셔너리를 만들어 출력
    
    3. 이 정보를 이용하여 학생의 학번을 입력받아
        이름과 전화번로를 출력하는 학사정보 프로그램을 작성
    
    4. student_tuple의 마지막 항목으로 학점을 추가
       이 정보를 바탕으로 딕셔너리를 만들어 출력
    
    5. 학생의 학점 평균을 출력
'''

# 학생 정보 튜플 작성
student_tuple = [("202095001", "홍길동", "010-1234-5678"), ("202095002", "김길동", "010-8765-4321"), ("202095003", "박길동", "010-1577-1577")]
student_dict = {} # 비어있는 딕셔너리 생성

# 딕셔너리 추가
for id, name, number in student_tuple :
    student_dict[id] = [name, number]
    
# 딕셔너리 출력
for key, value in student_dict.items() :
    print(key,":",value)
    
# 학번 입력 받아 이름과 연락처 출력
number = input("학번을 입력하세요 : ")
print("이름 :",student_dict[number][0])
print("연락처 :",student_dict[number][1])

# student_tuple의 마지막 항목으로 학점을 추가
student_dict['202095001'].append(4.5)
student_dict['202095002'].append(3.0)
student_dict['202095003'].append(3.5)

# 딕셔너리 출력
for key, value in student_dict.items() :
    print(key,":",value)

sum = 0
# 학점 평균 출력
for key, value in student_dict.items() :
    sum += value[-1]
 
print(f"학점 평균 : {sum/len(student_dict):.2f}")