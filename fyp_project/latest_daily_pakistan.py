import requests
from bs4 import BeautifulSoup
try:
    pagelink =requests.get('https://en.dailypakistan.com.pk/latest')
except:
    pass
if pagelink:
    soup=BeautifulSoup(pagelink.content,'html.parser')
    allnews=soup.findAll(class_='col-xs-12 col-sm-4 col-lg-3 verticle-widget-col news3')
    count=0
    latest_dailyPak_list={}
    for all_data in allnews:
        nani=all_data.find(class_='tt-news-img')
        link=nani.find('a')['href']
        get_image=nani.find('div').get('style')
        image_url=get_image.split('url(')[1].split(')')[0]
        news_title=nani.find('div').get('alt')
        latest_dailyPak_list[count]=[news_title,image_url,link,"Daily Pakistan"]
        count+=1