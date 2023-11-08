'''
    작성일 : 2023년 11월 8일
    작성자 : 컴퓨터공학부 2202395007 김수종
    설명 : 파티 동시 참석자 알아내기
'''
partyA = set(["Park", "Kim", "Lee"])
partyB = set(["Park", "Choi"])

print("2개의 파티를 모두 참석한 사람 :",partyA.intersection(partyB))
print("파티 A, B에 참석한 사람 :",partyA.union(partyB))
print("파티 A, B에 중복없이 참석한 사람 :",partyA.symmetric_difference(partyB))
print("파티 A에만 참석한 사람 :",partyA.difference(partyB))