'''
    작성일 : 2023년 9월 13일
    작성자 : 컴퓨터공학부 2202395007 김수종
    설명 : 직각 삼각형의 빗변의 길이를 구하기
'''

# 1. 밑변과 높이를 입력받아 변수에 저장
bttm = float(input("직각삼각형의 밑변의 길이를 입력하세요 : "))
higt = float(input("직각삼각형의 높이의 길이를 입력하세요 : "))

# 2. 빗변의 길이 게산 후 변수에 저장
hypo = (bttm**2 + higt**2)**0.5

# 3. 빗변의 길이 출력
print("밑변의 길이가 {}, 높이가 {}인 직각삼각형의 빗변의 길이는 {:.2f}".format(bttm,higt,hypo))