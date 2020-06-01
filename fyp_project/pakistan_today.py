from bs4 import BeautifulSoup
import requests
import pandas as pd

news_list_1 = {}
count = 0
url = "https://www.pakistantoday.com.pk/national"
for x in range(2,10):
    response = requests.get(url).text
    soup  =BeautifulSoup(response, 'html.parser')
    news = soup.find_all('article',{'class':'post'})
   
    for data in range(0,5):
        title = news[data].h2.text
        text = news[data].p.text
        image = news[data].find('div',{'class':'entry-thumbnail'}).a.img.get("src")
        link = news[data].h2.a.get("href")
        source = "PakistanToday"
        news_list_1[count] = [title,text,image,link,source]
        count+=1
    x = str(x)
    url = "https://www.pakistantoday.com.pk/national/page/"+x
 
    # df = pd.DataFrame.from_dict(news_list_1,orient='index', columns=['title','text','image','link','source'])
    # df.to_csv('latest_news_pakistantoday.csv', mode='a',header=False,index=False)


