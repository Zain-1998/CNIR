import requests
from bs4 import BeautifulSoup
pagelinkb =requests.get('https://nation.com.pk/Todays-Paper')
soupb=BeautifulSoup(pagelinkb.content,'html.parser')
allheading= soupb.findAll(class_='blocktitle')
bheading=allheading[1].get_text()
allbnews=soupb.findAll(class_='getcat')
bnews= allbnews[1]
bnewsimg= allbnews[1].find(class_='img_bckg')
bnewstit= allbnews[1].find(class_='ntitle')
for llopp in bnewstit.findAll('a'):
    blink=llopp
bnewstitle=allbnews[1].find(class_='ntitle').get_text()
finallistbusiness=[bheading,bnewsimg,bnewstitle,blink]
print(finallistbusiness)