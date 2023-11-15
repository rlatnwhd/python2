'''
    작성일 : 2023년 11월 15일
    작성자 : 컴퓨터공학부 2202395007 김수종
    설명 : 문자열
'''

# 문자열 슬라이싱
s = "Happy Day!"
print(s[0]) # 0
print(s[6:10]) # 6 ~ 9
print(s[:-2]) # 0 ~ 뒤에서 -2번째 까지

# 문자열 분리 : split()
# 분리한 후 리스트 형식으로 출력
s = "Welcom to Python"
print(s.split()) # 공백을 기준으로 분리

s = "2023.11.15"
print(s.split(".")) # "."을(를) 기준으로 분리

s = "Hello, World"
print(s.split(",")) # ","을(를) 기준으로 분리 (공백도 문자열)
print(s.split(", ")) # ", "을(를) 기준으로 분리

# 공백 제거 : strip()
s = "Welcome, to, Python, and, I, am, 신뢰에요"
print(s.strip())
print([x.strip() for x in s.split(",")])

print(list("Hello, World!")) # 한 글자씩 리스트에 저장(공백, 쉼표도 문자)

# 문자열 연결 : join()
print(','.join(["apple", "grape", "banana"])) # 각 항을 ","(으)로 연결

print('-'.join("010.1234.5678".split("."))) # "."을 기준으로 잘라서 리스트 형태로 나눈 후 "-"(으)로 연결

# 문자열 변경 : replace()
print("010.1234.5678".replace(".","-")) # "."(을)를 "-"(으)로 문자 변경

s = "Hello World!"
print(s)
# s에 저장된 문자열을 리스트로 문자열 분리 시켜 slist에 저장
slist = list(s)
print(slist)
# 분리된 문자열 다시 결합
print("".join(slist))

# 줄바꿈과 탭이 포함된 문자열 그대로 출력
a_string = "Today as well \n\t"
print(a_string)

# 문자열 자르기 word_list에 저장
word_list = a_string.split() # 공백을 기준으로 분리
print(word_list)

# 다시 결합 : 문자열을 분리시키고 다시 결합하면 줄바꿈(\n)과 탭(\t)이 삭제된다.
refined_string = " ".join(word_list)
print(refined_string)

# 대소문자 변환 : lower(), upper()
s = "Hello, World"
print(s)
print(s.lower()) # 모든 영문자를 소문자로 변환
print(s.upper()) # 모든 영문자를 대문자로 변환

# 공백 제거 : strip(), lstrip(), rstrip()
s = "          Hello, World              "
print(s.strip()) # 오,왼 모든 공백 제거
print(s.lstrip()) # 왼쪽의 모든 공백 제거
print(s.rstrip()) # 오른쪽의 모든 공백 제거

s = "###############Hello, World##################"
print(s.strip("#")) # 오,왼 모든 "#" 제거
print(s.lstrip("#")) # 왼쪽의 모든 "#" 제거
print(s.rstrip("#")) # 오른쪽의 모든 "#" 제거

# 문자열 찾기 (".kr" 찾기) : find()
s = "www.silla.ac.kr"
print(s.find(".kr")) # 해당 인덱스 번호를 출력
print(s.find("x")) # 해당 문자가 없으면 -1 출력

# 문자 개수 세기 : count()
print(s.count("."))