import requests
from bs4 import BeautifulSoup
pagelink =requests.get('https://profit.pakistantoday.com.pk/category/headlines')
soup=BeautifulSoup(pagelink.content,'html.parser')
allnews=soup.find(class_='td-ss-main-content')
newstit=allnews.findAll(class_='td_module_10 td_module_wrap td-animation-stack')
count=0
listt={}
list1={}
list2={}
list3={}
pakToday_business_list={}
for nani in newstit:
    image_url=nani.find(class_='td-image-wrap').find('img').get('data-img-url')
    listt[count]=image_url
    count+=1
count=0
for nani in newstit:
    link=nani.find(class_='item-details').find('a').get('href')
    news_title=nani.find(class_='item-details').find('a').get_text()
    list1[count]=news_title
    list2[count]=link
    list3[count]="Pakistan Today"
    count+=1
count=0
for count in range(0,len(newstit)):
    pakToday_business_list[count]=[list1[count],listt[count],list2[count],list3[count]]
