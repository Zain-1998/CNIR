import requests
from bs4 import BeautifulSoup
pagelink =requests.get('https://tribune.com.pk/life-style/')
soup=BeautifulSoup(pagelink.content,'html.parser')
getallnews=soup.find(class_='span-6 top-news')
allnews=getallnews.findAll(class_='content clearfix')
count=0
tribune_entertainment_list={}
for nani in allnews:
    link=nani.find('a')['href']
    image_url=nani.find('img').get('src')
    news_title=nani.find('h2').find('a').get_text()
    tribune_entertainment_list[count]=[news_title,image_url,link,"Express Tribune"]
    count+=1
