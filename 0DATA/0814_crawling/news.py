#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests as req
from bs4 import BeautifulSoup as bs

keyword = input("검색어를 입력하세요")
res = req.get(f"https://search.naver.com/search.naver?ssc=tab.news.all&where=news&sm=tab_jum&query={keyword}")
html = res.text
soup = bs(html, "lxml")

titles = soup.select(".news_tit")
count=1
for title in titles:
    print(count,title.text)
    print(title.attrs['href'])
    count +=1
input('입력 시 종료')

