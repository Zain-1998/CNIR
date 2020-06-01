import requests
from bs4 import BeautifulSoup
pagelinkn =requests.get('https://nation.com.pk/Todays-Paper')
soupn=BeautifulSoup(pagelinkn.content,'html.parser')
allheading= soupn.findAll(class_='blocktitle')
nheading=allheading[0].get_text()
allnnews=soupn.findAll(class_='getcat')
nnews= allnnews[0]
nnewsimg= allnnews[0].find(class_='img_bckg')
nnewstit= allnnews[0].find(class_='ntitle')
for lopp in nnewstit.findAll('a'):
    nlink=lopp
nnewstitle=allnnews[0].find(class_='ntitle').get_text()
finallistnational=[nheading,nnewsimg,nnewstitle,nlink]
print(finallistnational)