import requests
from bs4 import BeautifulSoup
pagelink =requests.get('https://paperazzi.pakistantoday.com.pk/category/entertainment')
soup=BeautifulSoup(pagelink.content,'html.parser')
allnews=soup.find(class_='mvp-feat1-list left relative mvp-tab-col-cont')
newstit=allnews.findAll(class_='mvp-feat1-list-img left relative')
newstit1=allnews.findAll(class_='mvp-feat1-list-text')
count=0
listt={}
list1={}
list2={}
list3={}
pakToday_entertainment_list={}
for nani in allnews.findAll('a'):
    link=nani.get('href')
    list2[count]=link
    count+=1
count=0
for nani in newstit:
    image_url=nani.find('img').get('src')
    listt[count]=image_url
    count+=1
count=0
for nani1 in newstit1:
    news_title=nani1.find('h2').get_text()
    list1[count]=news_title
    list3[count]="Pakistan Today"
    count+=1
count=0
for count in range(0,len(newstit)):
    pakToday_entertainment_list[count]=[list1[count],listt[count],list2[count],list3[count]]
