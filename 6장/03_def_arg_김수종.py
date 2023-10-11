'''
    작성일 : 2023년 10월 11일
    작성자 : 컴퓨터공학부 2202395007 김수종
    설명 : 함수에 여러 개의 값 넘겨주기
    
    두 수를 입력받아 함수를 호출하여 두 수 사이의 합을 계산하여 돌려주는 함수
    
    [알고리즘]
    (함수)
        3. 두 수를 전달받아 매개 변수에 저장
        4. 두 수 사이의 합을 계산
        5. 계산된 합을 함수를 호출한 곳으로 돌려줌
    (메인)
        1. 두 수 입력받기
        2. 두 수를 가지고 함수 호출
        6. 돌려받은 합을 출력
'''

print(":: 두 수 사이의 합 구하기 (매개 변수가 두 개인 함수) ::")

# 함수 선언
def get_sum(num1, num2) :
    sum=0
    if num1 > num2 :
        start=num2
        fin=num1
    else :
        start=num1
        fin=num2
    for i in range(start, fin+1) :
        sum+=i
    return sum

start = int(input("시작 수 입력 : "))
end = int(input("종료 수 입력 : "))

sum = get_sum(start, end)

print(f"{start}와(과) {end} 사이의 합 : {sum}")