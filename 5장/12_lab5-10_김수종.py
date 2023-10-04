'''
    작성일 : 2023년 10월 4일
    작성자 : 컴퓨터공학부 2202395007 김수종
    설명 : 사용자에게 숫자를 입력받아 그 합을 출력하는 프로그램
           
           문제 분석 : "yes"를 입력 받으면 반복
                       "no"와 그 나머지를 입력 받으면 반복 종료
                       합계 출력
           필요한 변수 : sum, answer, num
'''

print(":: 반복 변수 지정 ::")
# 1. 합게 초기 값 지정
sum = 0

# 2. 무한 반복할 변수 지정
answer = "yes"

# 3. "yes"를 입력 받으면 게속 수를 입력받고, "no"와 그 나머지를 입력 받으면 종료
while answer == "yes" :
    num = int(input("숫자를 입력하세요 : "))
    sum += num      # 합계 누적
    answer = input("게속?(yes/no) : ")

print("합계는 :",sum)   # 합계 출력

print() # 한 줄 띄우기

print(":: break 사용 ::")
# 1. 합게 초기 값 지정
sum = 0

# 2. "yes"를 입력 받으면 게속 수를 입력받고, "no"와 그 나머지를 입력 받으면 break를 사용하여 종료
while True :
    num = int(input("숫자를 입력하세요 : "))
    sum += num      # 합계 누적
    answer = input("게속?(yes/no) : ")
    if answer != "yes" :
        break

print("합계는 :",sum)   # 합계 출력