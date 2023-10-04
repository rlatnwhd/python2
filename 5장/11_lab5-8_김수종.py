'''
    작성일 : 2023년 10월 4일
    작성자 : 컴퓨터공학부 2202395007 김수종
    설명 : 별 그리기
'''

import turtle as t
t.speed(2)
t.shape("turtle")

count = 0 

t.left
while count <= 4 :
    t.fd(50)
    t.right(144)
    count += 1
    
t.mainloop()