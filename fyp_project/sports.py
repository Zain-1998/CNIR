import requests
from bs4 import BeautifulSoup

pagelink =requests.get('https://nation.com.pk/Todays-Paper')
soupsp=BeautifulSoup(pagelink.content,'html.parser')
allheading= soupsp.findAll(class_='blocktitle')
spheading=allheading[6].get_text()
allspnews=soupsp.findAll(class_='getcat')
spnews= allspnews[6]
spnewsimg= allspnews[6].find(class_='img_bckg')
spnewstit= allspnews[6].find(class_='ntitle')
for l in spnewstit.find_all('a'):
    link=l
spnewstitle=allspnews[6].find(class_='ntitle').get_text()
finallist=[spheading,spnewsimg,spnewstitle,link]