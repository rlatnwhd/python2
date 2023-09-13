'''
    작성일 : 2023년 9월 13일
    작성자 : 컴퓨터공학부 2202395007 김수종
    설명 : 피자의 면적 구하기
            - 피자의 반지름이 필요
            - 피자의 반지름은 입력받아 게산
'''

# 1. 반지름을 입력 받아 변수에 저장
radius = int(input("피자의 반지름을 입력하세요 : "))
PI = 3.14 # 3.14는 상수 -> 대문자로 변수 생성

# 2. 피자의 면적 게산
area = PI*radius**2

# 3. 피자의 면적 출력
# 반지름이 0인 피자의 면적은 00.00
print("반지름이 {}인 피자의 면적은 {:.2f}".format(radius,area))