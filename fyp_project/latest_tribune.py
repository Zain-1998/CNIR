import requests
from bs4 import BeautifulSoup
pagelink =requests.get('https://tribune.com.pk/latest-news/')
soup=BeautifulSoup(pagelink.content,'html.parser')
allnews=soup.findAll(class_='story cat-0 group-0 position-0 couplet clearfix')
count=0
latest_tribune_list={}
for nani in allnews:
    image_url=nani.find('img').get('src')
    news_title=nani.find('h2').find('a').get_text()
    link=nani.find('h2').find('a').get('href')
    latest_tribune_list[count]=[news_title,image_url,link,"Express Tribune"]
    count+=1