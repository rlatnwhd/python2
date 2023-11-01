'''
    작성일 : 2023년 11월 1일
    작성자 : 컴퓨터공학부 2202395007 김수종
    설명 : LAB 7-5 함수는 튜플을 졸려줄 수 있다.
    
        반지름을 입력받아 원의 넓이와 둘레를 계산하시오.
        넓이와 둘래를 계산하는 함수를 작성하시오.
        함수는 넓이와 둘레를 함께 돌려줍니다.
        
        [함수]
            3. 반지름을 받아서 매개변수에 저장
            4. 넓이와 둘레를 계산
            5. 넓이와 둘레를 리턴 (함수를 호출한 곳으로)
               return (넓이), (둘레)
        
        [메인]
            1. 반지름을 입력받음
            2. 함수 호출 -> 반지름을 가지고 호출
            6. 돌려받은 넓이와 둘레를 튜플로 저장
               ((넓이), (둘레))
            7. 출력
'''

import math as m

def calcircle(r):
    area = m.pi * r * r
    circum = 2 * m.pi * r
    return (area, circum)

radius = int(input("원의 반지름을 입력하세요 : "))

(area, circum) = calcircle(radius)

print(f"반지름이 {radius}인 원의 넓이는 {area:.2f}, 원의 둘레는 {circum:.2f}이다.")

circle = calcircle(radius)
print(f"반지름이 {radius}인 원의 넓이는 {circle[0]:.2f}, 원의 둘레는 {circle[1]:.2f}이다.")