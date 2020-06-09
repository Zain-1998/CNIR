import requests
from bs4 import BeautifulSoup
pagelink =requests.get('https://www.pakistantoday.com.pk/national')
soup=BeautifulSoup(pagelink.content,'html.parser')
allnews=soup.find(class_='content-inner layout-')
newstit=allnews.findAll(class_='entry-thumbnail')
newstit1=allnews.findAll(class_='entry-content')
count=0
list={}
list1={}
list2={}
list3={}
latest_pakToday_list={}
for nani in newstit:
    image_url=nani.find('img').get('src')
    list[count]=image_url
    count+=1
count=0
for nani1 in newstit1:
    link=nani1.find('a').get('href')
    news_title=nani1.find('a').get_text()
    list1[count]=news_title
    list2[count]=link
    list3[count]="Pakistan Today"
    count+=1
count=0
for count in range(0,len(newstit)):
    latest_pakToday_list[count]=[list1[count],list[count],list2[count],list3[count]]
 
    # df = pd.DataFrame.from_dict(news_list_1,orient='index', columns=['title','text','image','link','source'])
    # df.to_csv('latest_news_pakistantoday.csv', mode='a',header=False,index=False)


