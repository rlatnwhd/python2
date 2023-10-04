'''
    작성일 : 2023년 10월 4일
    작성자 : 컴퓨터공학부 2202395007 김수종
    설명 : 조건에 따라 반복하는 while문
           교재 129p 
           
           1 ~ 10 까지의 합계를 계산하여 출력하기
           시작 값 : 1
           종료 값 : 10
           증가 값 : 1
           for i in range(1, 11) : => while 문으로 바꾸기
           
           필요한 변수 : count, sum
'''

count = 1   # 시작 값
sum = 0     # 합계 계산을 위한 초기 값 지정

while count <= 10 :     # 종료 값 (조건식)
    sum += count
    count += 1      # 증가 값 =(count = count + 1)

print("합계는 :",sum)