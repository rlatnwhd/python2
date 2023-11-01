'''
    작성일 : 2023년 11월 1일
    작성자 : 컴퓨터공학부 2202395007 김수종
    설명 : 한번 생성하면 그 값을 고칠 수 없는 자료형 : 튜플
'''

# 리스트 생성
color_list = ['red', 'green', 'blue', 'orange']
# 튜플 생성
color = ('red', 'green', 'blue', 'orange')
print(f"color : {color}")

# color 에 black 추가하기
# AttributeError: 'tuple' object has no attribute 'append'
# 특성 오류: 'tuple' 개체에 'append' 속성이 없습니다.
# tuple 자료형은 추가 및 삭제가 불가능
# color.append('black')

# 인덱싱돠 슬라이싱은 문자열이나 리스트와 동일하게 동작한다.
print("color 튜플 : ", color)
print("color 튜플 중 2, 3, 4번 : ", color[1:4])
print("color 튜플 중 처음 ~ 3번 : ", color[:3])
print("color 튜플 중 3번 ~ 끝 : ", color[2:])
print("color 튜플 중 1, 3, 5번 : ", color[::2])
print("color 튜플 중 거꾸로 출력 : ", color[::-1])

# 튜플 끼리의 결합 => '+' 연산자 / 반복 => '*' 연산자
colors = color + color
print(f"colors 튜플 : {colors}")
print(f"color 튜플을 10번 반복 : {color*10}")