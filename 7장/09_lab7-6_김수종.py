'''
    작성일 : 2023년 11월 1일
    작성자 : 컴퓨터공학부 2202395007 김수종
    설명 : LAB 7-6 도시의 이름과 인구를 튜플로 묶어보자
'''

# 다음과 같은 리스트가 생성되어 있다
city_info = [('서울', 9765),('부산', 3441), ('광주', 1501), ('대전',1531)]

max_population = city_info[0][1] # city_info의 인덱스 0번지의 튜플 1번지 값을 초기 최대값으로 지정
min_population = city_info[0][1] # city_info의 인덱스 0번지의 튜플 1번지 값을 초기 최소값으로 지정
total_population = 0 # 평균 인구수 초기화

max_city = None # 최대인구 도시 저장값 초기화
min_city = None # 최소인구 도시 저장값 초기화

for city, population in city_info:  # (도시명), (인구수)
    total_population += population
    if population > max_population:
        max_population = population
        max_city = city
    if population < min_population:
        min_population = population
        min_city = city
        
print(f"최대인구 : {max_city} | 인구 : {max_population}천명")
print(f"최소인구 : {min_city} | 인구 : {min_population}천명")
print(f"리스트 도시 평균 인구 : {total_population/len(city_info)}천명")