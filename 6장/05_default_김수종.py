'''
    작성일 : 2023년 10월 11일
    작성자 : 컴퓨터공학부 2202395007 김수종
    설명 : 함수의 디폴트 인자
'''

def order(num, pickel, onion) :
    print("행버거 {}개 - 피클 {}개, - 양파 {}개".format(num, pickel, onion))

# order(1) # 오류 발생, 인자는 1개인데 매개변수는 3개

# 인자가 부족한 경우 기본값을 넣어주는 것 -> 디폴트 인자
def order2(num, pickel="기본", onion="기본") :
    print("행버거 {}개 - 피클 {} - 양파 {}".format(num, pickel, onion))
    
order2(1)
order2(1, pickel="뺌", onion="기본")