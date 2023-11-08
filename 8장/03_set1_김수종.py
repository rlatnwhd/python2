'''
    작성일 : 2023년 11월 8일
    작성자 : 컴퓨터공학부 2202395007 김수종
    설명 : 집합 set()
'''

# 빈 집합 만들기
number = set()

# 숫자 3개로 이루어진 집합
number1 = {2, 1, 3}
print("집합 : ",number1) # 정렬처럼 보이지만 실제로는 아님

# 리스트로 부터 집합 생성
number2 = set([1, 2, 3, 1, 2])
print("집합 : ",number2) # 중복을 허용하지 않는다

text1 = set("asdfasdf")
print("집합 : ",text1) # 순서가 없어 지쪼대로 출력된다

numbers = {2, 4, 5, 1, 2}
if 1 in numbers : # 집합 안에 1이 포함되어 있는가
    print("집합에 1이 있습니다.")
    
# 집합은 순서가 없어 index로 접근이 불가능하다
# 반복문으로 접근하여 출력이 가능하다

numbers = {9, 1, 5, 2, 4, 7, 6, 3, 4, 9, 1, 8}
for num in numbers :
    print(num, end=' ')

print()

# 정렬 후 출력
for num in sorted(numbers) :
    print(num, end=' ')
    
print()
    
# 추가하기 (순서가 없어서 아무곳에다가 추가함) 
numbers.add(100)
for num in sorted(numbers) :
    print(num, end=' ')

print()

# 삭제하기
numbers.remove(100)
for num in sorted(numbers) :
    print(num, end=' ')