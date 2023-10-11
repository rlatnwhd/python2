'''
    작성일 : 2023년 10월 11일
    작성자 : 컴퓨터공학부 2202395007 김수종
    설명 : LAB 6-4 리스트에서 최대값, 최소값을 찾아 돌려주는 함수
    
    리스트에서 10개의 값을 랜덤으로 생성하고,
    max 또는 min을 입력 받아 최대, 최소값을 찾아 돌려주는 함수
    
    [알고리즘]
    (함수)
            5) 두 값을 전달받아 매개 변수 저장
            6) 최대값, 최소값을 구하기
            7) 값을 돌려준다
    (메인)
        1. 무한 반복
            1) 랜덤으로 10에서 99까지 10개의 난수를 리스트로 생성
            2) 생성된 리스트를 출력
            3) 사용자로부터 최대값을 알고싶은지 최소값을 알고싶은지 질문
              (사용자가 입력할 값 : max 또는 min)
            4) 입력받은 max 또는 min과 생성된 리스트를 가지고 함수 호출
            8) 돌려 받는 최대값 또는 최소값 출력
'''

import random as r

def maxmin(choose, list):
    if choose == "min" :
        result = min(list)
    elif choose == "max" :
        result = max(list)
    else :
        return
    return result

while(1):
    randomlist = []
    for i in range(1, 11):
        randomlist.append(r.randint(10,99))
    print(randomlist)
    choose=input("최대값을 원하면 'max', 최소값을 원하면 'min' 을 입력하세요(그 외는 None 출력함) : ")
    print(maxmin(choose, randomlist))
    
