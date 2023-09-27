'''
    작성일 : 2023년 9월 27일
    작성자 : 컴퓨터공학부 2202395007 김수종
    설명 : 점수를 입력받아 학점을 출력하시오.
            90 ~ 100 : A학점
            80 ~ 89  : B학점
            70 ~ 79  : C학점
            60 ~ 69  : D학점
            0 ~ 59   : F학점
            
    알고리즘 ->
    1. 점수를 입력 받기
    2. 판단하여 출력하기
'''

# 점수 입력 받기
score = int(input("점수 입력 : "))

# 판단
# 이 코드는 논리 오류가 발생한다 - 100점 이상의 값을 입력 시 무조건 A학점
print(":: 첫 번째 성적 처리 ::")
if score >= 90 :
    print("A학점")
elif score >= 80 :
    print("B학점")
elif score >= 70 :
    print("C학점")
elif score >= 60 :
    print("D학점")
else :
    print("F학점")
    
print()    # 빈줄 출력

# 정확한 범위를 지정한다 - 성적의 범위를 벗어나면 "잘못된 점수입니다." 출력
'''
    90 ~ 100 : A학점
    80 ~ 89  : B학점
    70 ~ 79  : C학점
    60 ~ 69  : D학점
    0 ~ 59   : F학점

'''
print(":: 두 번째 성적 처리 ::")
if 100 >= score >= 90 :
    print("A학점")
elif 90 > score >= 80 : # = (score >= 80 and score < 90) -> C언어 (score >= 80 && score < 90)
    print("B학점")
elif 80 > score >= 70 :
    print("C학점")
elif 70 > score >= 60 :
    print("D학점")
elif 60 > score >= 0 :
    print("F학점")
else :
    print("잘못된 점수입니다.")
    
print()    # 빈줄 출력

# 점수는 무조건 0~100점 사이입니다. - 혹은 잘못된 입력입니다.
print(":: 세 번째 성적 처리 ::")
if 0 <= score <= 100 :
    if score >= 90 :
        print("A학점")
    elif score >= 80 :
        print("B학점")
    elif score >= 70 :
        print("C학점")
    elif score >= 60 :
        print("D학점")
    else : # A, B, C, D 학점이 아니면
        print("F학점")
else : # 0~100 사이의 점수가 아니면
    print("잘못된 점수입니다.")