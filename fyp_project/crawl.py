import numpy as np
import pandas as pd
import requests
import bs4


news = input("Enter Your Search Query!! ")
my_data = {}
all_news= 0
res = requests.get('https://news.google.com/search?q='+news)
soup = bs4.BeautifulSoup(res.text, "html.parser")
search_result = soup.find_all('div',{'class':'NiLAwe'})
for i in search_result:
        title = i.article.h3.text
        text = i.article.div.span.text
        source = i.find('a',{'class':'wEwyrc AVN2gc uQIVzc Sksgp'}).text
        link = i.a.get('href')
        link = "https://www.news.google.com/"+link
        my_data[all_news] = [title,text,source,link]
        print("------------ NEXT NEWS -----------------")
        all_news+=1
        print(title)
        print(text)
        print(source)
        print("-------------End Of News-----------------")
  #  df = pd.DataFrame.from_dict(my_data,orient='index', columns=['title','text','link','source'])
  #  df.to_csv('data.csv', mode='w',header=True,index=False)


