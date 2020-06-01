import requests
from bs4 import BeautifulSoup
pagelinken =requests.get('https://nation.com.pk/Todays-Paper')
soupen=BeautifulSoup(pagelinken.content,'html.parser')
allheading= soupen.findAll(class_='blocktitle')
enheading=allheading[7].get_text()
allenews=soupen.findAll(class_='getcat')
enews= allenews[7]
enewsimg= allenews[7].find(class_='img_bckg')
enewstit= allenews[7].find(class_='ntitle')
for loopp in enewstit.findAll('a'):
    elink=loopp
enewstitle=allenews[7].find(class_='ntitle').get_text()
finallistent=[enheading,enewsimg,enewstitle,elink]
print(finallistent)
