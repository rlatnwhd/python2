'''
    작성일 : 2023년 10월 11일
    작성자 : 컴퓨터공학부 2202395007 김수종
    설명 : 함수에 여러 개의 값 넘겨주고 여러 개의 값을 돌려 받기
    
    두 수를 전달받아 사칙연산의 결과 값을 돌려주는 함수
    
    [알고리즘]
    (함수)
        3. 전달받은 2개의 값을 매개 변수에 저장5
        4. 두 수를 가지고 사칙연산(+,-,*,/,%)을 계산
        5. 사칙연산의 결과 5개를 돌려줌
    (메인)
        1. 두 수를 입력받기
        2. 두 수를 가지고 함수 호출
        6. 돌려받은 결과값 출력
'''

print(":: 두 수 사이의 합 구하기 (리턴 값이 두 개인 함수) ::")

# 함수 선언
def cals(num1, num2) :
    sum = num1 + num2
    minus = num1 - num2
    mul = num1 * num2
    div = num1 / num2
    rest = num1 % num2
    return sum, minus, mul, div, rest # 돌려주는 결과는 5개

num1 = int(input("첫 번째 정수 입력 : "))
num2 = int(input("두 번째 정수 입력 : "))

sum, minus, mul, div, rest = cals(num1, num2)
print(f"{num1}와(과) {num2}의 사칙연산")
print(f"{num1} + {num2} = {sum}")
print(f"{num1} - {num2} = {minus}")
print(f"{num1} * {num2} = {mul}")
print(f"{num1} / {num2} = {div}")
print(f"{num1} % {num2} = {rest}")