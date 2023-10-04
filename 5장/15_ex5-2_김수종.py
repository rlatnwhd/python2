'''
    작성일 : 2023년 10월 4일
    작성자 : 컴퓨터공학부 2202395007 김수종
    설명 : 두 수를 입력 받아 ->
            1. 두 수 사이의 짝수의 합계
            2. 두 수 사이의 짝수의 합계 출력
            
            심화 문제 5-2, 141p
            for 또는 while 원하는 것 사용
'''

# 1. 두 수를 입력받아 변수에 저장
num1 = int(input("첫 번째 숫자 입력 : "))
num2 = int(input("두 번째 숫자 입력 : "))

# 2. 두 수의 합계, 두 수 사이 짝수의 합계 기초 값 지정
sum = 0
even_sum = 0

# 3. 시작 값 지정
if num1 > num2 :
    start=num2
    fin=num1
else :
    start=num1
    fin=num2

while start <= fin :
    sum += start    # 합계 누적
    if start % 2 != 0 :     # 짝수가 아니면
        start+=1
        continue    # 밑 문장 실행하지 않고 반복문 처음으로 돌림
    even_sum+=start   # 짝수 합계 누적
    start+=1     # start가 1씩증가

print(f"{num1}와(과) {num2}의 사이의 합 : {sum}")
print(f"{num1}와(과) {num2}의 사이 짝수의 합 : {even_sum}")