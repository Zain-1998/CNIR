import requests
from bs4 import BeautifulSoup
pagelink =requests.get('https://nation.com.pk/entertainment')
soup=BeautifulSoup(pagelink.content,'html.parser')
allnews=soup.find(class_='blogtwo blogthree')
newstit=allnews.findAll(class_='ntitle')
newstit1=allnews.findAll(class_='lthumb')
count=0
nation_entertainment_list={}
list1={}
list2={}
list3={}
list4={}
for nani in newstit:
    link=nani.find('a').get('href')
    news_title=nani.find('a').get_text()
    list1[count]=link
    list2[count]=news_title
    count+=1
count=0
for nani1 in newstit1:
    get_image=nani1.find('div').get('style')
    image_url=get_image.split('url(')[1].split(')')[0]
    list3[count]=image_url
    list4[count]="The Nation"
    count+=1
count=0
for count in range(0,len(newstit)):
    nation_entertainment_list[count]=[list2[count],list3[count],list1[count],list4[count]]