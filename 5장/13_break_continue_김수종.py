'''
    작성일 : 2023년 10월 4일
    작성자 : 컴퓨터공학부 2202395007 김수종
    설명 : 반복을 제어하는 break, continue
           교재 137p
           
    Test word : programming
'''

word = input("단어를 입력하세요 : ")    # 단어를 입력 받아 변수에 저장

print(":: break 1 ::")
for i in word : # 단어 갯수만큼 반복
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u" :     # 알파벳이 모음이면
        break   # 반복문 정지 (포함된 반복문이 종료)
    else :
        print(i,end="")     # 결과 : pr

print()   # 한 줄 띄우기

print(":: break 2 ::")
for i in word : 
    if i in ["a","e","i","o","u","A","E","I","O","U"] :
        break  
    else :
        print(i,end="")     # 결과 : pr

print()   # 한 줄 띄우기

print(":: continue 2 ::")
for i in word : 
    if i in ["a","e","i","o","u","A","E","I","O","U"] :
        continue    # 아래 문장을 실행 시키지 않고 다시 반복문의 처음으로 돌아감
    print(i,end="")     # 결과 : prgrmmng