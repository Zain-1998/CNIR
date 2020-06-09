import requests
from bs4 import BeautifulSoup
pagelink =requests.get('https://en.dailypakistan.com.pk/pakistan')
soup=BeautifulSoup(pagelink.content,'html.parser')
allnews=soup.findAll(class_='col-sm-6')
count=0
dailyPak_pakistan_list={}
for all_data in allnews:
    nani=all_data.find(class_='tt-news-img')
    link=nani.find('a')['href']
    get_image=nani.find('div').get('style')
    image_url=get_image.split('url(')[1].split(')')[0]
    news_title=nani.find('div').get('alt')
    dailyPak_pakistan_list[count]=[news_title,image_url,link,"Daily Pakistan"]
    count+=1