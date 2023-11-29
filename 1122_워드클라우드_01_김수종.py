# -*- coding: utf-8 -*-
"""1122_워드클라우드_01.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15p73DPhygCI5QrQB9KBcNmV7FHMRw9vm

# 1. AI 워드 클라우드
"""

# 워드 클라우드 위기피디어 사용을 위한 패키지 설치
!pip install wordcloud wikipedia

# 데이터 시각화를 위한 멧플룻립 패키지 설치
!pip install matplotlib

# 라이브러리 가져오기
import wikipedia
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

# 위키피디아에서 컨텐츠 제목을 가져온다.
wiki = wikipedia.page('Artificial intelligence')

# 이 페이지의 텍스트 컨텐츠를 추출한다.
text = wiki.content

# 텍스트를 가지고 워드클라우드 생성.
wc = WordCloud(width=400, height=400).generate(text)

# 새로운 figure를 생성한다.
plt.figure(figsize=(10,10))

# wc를 이미지로 표시
plt.imshow(wc)

# 그래프를 화면에 출력
plt.show()

# 워드클라우드 저장
wc.to_file('AI_클라우드1.png')

# 중지어가 제외된 워드 클라우드 만들기
# 집합 -> 중복을 허용하지 않는다 => union(교집합)
s_word = STOPWORDS.union({'one','two','using','output','way','tool','step','use','make','area','well','layer','AI'})

# 위키피디아에서 컨텐츠 제목을 가져온다.
wiki = wikipedia.page('Artificial intelligence')

# 이 페이지의 텍스트 컨텐츠를 추출한다.
text = wiki.content

# 텍스트를 가지고 워드클라우드 생성.
wc = WordCloud(width=400, height=400, stopwords=s_word).generate(text)

# 새로운 figure를 생성한다.
plt.figure(figsize=(10,10))

# wc를 이미지로 표시
plt.imshow(wc)

# 그래프를 화면에 출력
plt.show()

# 워드클라우드 저장
wc.to_file('AI_클라우드2.png')