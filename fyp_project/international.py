import requests
from bs4 import BeautifulSoup
pagelinkin =requests.get('https://nation.com.pk/Todays-Paper')
soupin=BeautifulSoup(pagelinkin.content,'html.parser')
allheading= soupin.findAll(class_='blocktitle')
inheading=allheading[5].get_text()
allinnews=soupin.findAll(class_='getcat')
innews= allinnews[5]
innewsimg= allinnews[5].find(class_='img_bckg')
innewstit= allinnews[5].find(class_='ntitle')
for lop in innewstit.findAll('a'):
    inlink=lop
innewstitle=allinnews[5].find(class_='ntitle').get_text()
finallistinter=[inheading,innewsimg,innewstitle,inlink]
print(finallistinter)