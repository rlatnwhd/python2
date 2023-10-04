'''
    작성일 : 2023년 10월 4일
    작성자 : 컴퓨터공학부 2202395007 김수종
    설명 : 조건에 따라 반복하는 while문
           교재 127p 
'''

# while 조건식 : => 반드시 사용
#       들여쓰기를 반복하면서 사용
# 반복문에서는 반드시 종료 조건이 있어야 한다.
# while True :      무한 반복

under_construction = True   # 공사중(bool형)

# True 동안 계속 반복 (무한반복)
while under_construction :
    response = input("공사가 완료 되었습니까? : ")
    if response == "예" :
        under_construction = False      # 공사 완료(bool형) == break

print("- 루프 탈출 -")