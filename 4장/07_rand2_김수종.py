'''
    작성일 : 2023년 9월 20일
    작성자 : 컴퓨터공학부 2202395007 김수종
    설명 : 선택문 if~else
            random을 이용한 가위바위보 게임
            
            random함수로 생성된 정수를 가지고 게임을 진행
            0 -> 가위
            1 -> 바위
            2 -> 보
            
            두 명의 플레이어의 이름을 입력 받아 가위바위보 게임을 진행
'''
import random as r

print(":: 가위바위보 게임 시작 ::")

player1 = input("Player1 이름 입력 : ")
player2 = input("Player2 이름 입력 : ")

num1 = r.randrange(3) # player1의 랜덤 수
num2 = r.randrange(3) # player2의 랜덤 수

# Player1의 가위 바위 보 출력
print(f"{player1} :", end=" ")
if num1 == 0 :
    print("가위!")
elif num1 == 1 :
    print("바위!")
else :
    print("보!")

# Player2의 가위 바위 보 출력
print(f"{player2} :", end=" ")
if num2 == 0 :
    print("가위!")
elif num2 == 1 :
    print("바위!")
else :
    print("보!")
    
# 결과 출력
if (num1 == 0 and num2 == 2) or (num1 == 1 and num2 == 0) or (num1 == 2 and num2 == 1) :
    print(player1,"승리!")
elif num1 == num2:
    print("무승부!")
else :
    print(player2,"승리!")