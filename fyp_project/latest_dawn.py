import requests
from bs4 import BeautifulSoup
pagelink =requests.get('https://www.dawn.com/latest-news')
soup=BeautifulSoup(pagelink.content,'html.parser')
getallnews=soup.find(class_='tabs__pane active')
allnews=getallnews.findAll('article')
count=0
latest_dawn_list={}
for all_data in allnews:
    nani=all_data.find(class_='media__item')
    link=nani.find('a')['href']
    image_url=nani.find('img').get('src')
    news_title=nani.find('img').get('alt')
    latest_dawn_list[count]=[news_title,image_url,link,"Dawn"]
    count+=1
# df = pd.DataFrame.from_dict(news_list,orient='index', columns=['title','text','image','link','source'])
# df.to_csv('latest_news_dawnnews.csv', mode='a',header=False,index=False)