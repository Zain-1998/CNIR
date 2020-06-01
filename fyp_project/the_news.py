from bs4 import BeautifulSoup
import requests
import pandas as pd

url = "https://www.thenews.com.pk/latest-stories"
news_list = {}
news_no =0 
response = requests.get(url).text
soup  =BeautifulSoup(response, 'html.parser')
news = soup.find_all('div',{'class':'latest-right'})
for newss in range(0,5):  
    title = news[newss].h2.a.text
    text = news[newss].p.text
    image = "None"
    links = news[newss].h2.a.get('href')
    source = "TheNews"
    news_list[news_no] = [title, text, image, links,source]
    news_no+=1
# df = pd.DataFrame.from_dict(news_list,orient='index', columns=['title','text','image','link','source'])
# df.to_csv('latest_news_dawnnews.csv', mode='a',header=False,index=False)
