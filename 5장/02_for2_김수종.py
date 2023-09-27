'''
    작성일 : 2023년 9월 27일
    작성자 : 컴퓨터공학부 2202395007 김수종
    설명 : 반복문 for 사용하기
'''

# 본인 이름 5개 출력
print(":: 내 이름 5개 출력하기 ::")
for i in range(5): 
    print(i," : 김수종")

print()    # 빈줄 출력

print(":: 내 이름 5개 출력하기(리스트) ::")
for i in [1,2,3,4,5]: # 리스트
    print(i," : 김수종")
    
print()    # 빈줄 출력

print(":: 리스트로 구구단의 19단 출력 ::")
for num in [1,2,3,4,5,6,7,8,9]: # for i in range(1,10):
    print(f"19 X {num} = {19*num}")
    
print()    # 빈줄 출력

print(":: 문자열 내용 출력 ::")
for i in "Hello" : # 문자열
    print("i =", i)
        
print()    # 빈줄 출력

# 도전 문제 5.3
print(":: BTS 멤버 명단 출력 ::")
bts = ['뷔', '제이홉', 'RM', '정국', '진', '지민', '슈가'] # 리스트를 변수에 저장해서 출력
for i in bts:
    print(i)