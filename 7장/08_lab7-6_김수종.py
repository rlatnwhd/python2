'''
    작성일 : 2023년 11월 1일
    작성자 : 컴퓨터공학부 2202395007 김수종
    설명 : LAB 7-6 도시의 이름과 인구를 튜플로 묶어보자
'''

# 다음과 같은 리스트가 생성되어 있다
city_info = [('서울', 9765),('부산', 3441), ('광주', 1501), ('대전',1531)]

max_population = 0 # 최대 인구수를 구하기 위해 작은 수 저장 / 작은 수를 해야 0 이상의 최대값을 저장할 수 있음
min_population = 99999999999999999999 # 최소 인구수를 구하기 위해 큰 수 저장 / 큰 수를 해야 제일 작은 최소값을 저장할 수 있음(0을 해버리면 0이 제일 작은 최소값이 될 수도 있음)
total_population = 0 # 평균 인구수 초기화

max_city = None # 최대인구 도시 저장값 초기화
min_city = None # 최소인구 도시 저장값 초기화

for city in city_info:  # city_info 리스트 내용만큼 반복 (city변수 사용)
    total_population += city[1] # city_info 리스트에서 가져온 변수(튜플)에서 인덱스 1번지를 누적(인구수)
    if city[1] > max_population: # 변수(튜플)의 인덱스 1번지(인구수)가 최대 인구수보다 크면 실행
        max_population = city[1] # 변수(튜플)의 인덱스 1번지(인구수)를 max_population에 저장
        max_city = city # 변수(튜플)를 최대 인구 도시에 저장
    if city[1] < min_population: # 변수(튜플)의 인덱스 1번지(인구수)가 최소 인구수보다 작으면 실행
        min_population = city[1] # 변수(튜플)의 인덱스 1번지(인구수)를 min_population에 저장
        min_city = city # 변수(튜플)를 최소 인구 도시에 저장
        
print(f"최대인구 : {max_city[0]} | 인구 : {max_population}천명") # max_city의 인덱스 0번 출력(최대인구 도시), max_population(최대 인구수) 출력
print(f"최소인구 : {min_city[0]} | 인구 : {min_population}천명") # min_city의 인덱스 0번 출력(최소인구 도시), min_population(최대 인구수) 출력
print(f"리스트 도시 평균 인구 : {total_population/len(city_info)}천명") # 총 누적 값을 city_info의 원소 개수만큼 나누어 평균 출력