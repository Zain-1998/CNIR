import requests
from bs4 import BeautifulSoup
pagelink =requests.get('https://www.dawn.com/sport')
soup=BeautifulSoup(pagelink.content,'html.parser')
allnews=soup.findAll(class_='flex__item sm:w-1/4 w-full')
count=0
dawn_sports_list={}
for all_data in allnews:
    newstit=all_data.findAll(class_='media__item')
    for nani in newstit:
        try:
            link=nani.find('a')['href']
            image_url=nani.find('img').get('src')
            news_title=nani.find('img').get('alt')
        except:
            break
        dawn_sports_list[count]=[news_title,image_url,link,"Dawn"]
        count+=1