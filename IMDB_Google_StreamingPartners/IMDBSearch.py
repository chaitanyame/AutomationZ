from bs4 import BeautifulSoup
import requests
import os
import sys
import time
import json


p= requests.get('https://www.imdb.com/india/top-rated-malayalam-movies')
soup=BeautifulSoup(p.content,'html.parser')
lists=[]
for a in soup.findAll('img', alt=True,):
    lists.append(a['alt'])

for li in lists:
    SearchStr=str(li).replace(" ","+")
    FinalURl='https://www.google.com/search?q={0}'.format(SearchStr)

    session = requests.Session()
    headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36"}
    moviesoup=BeautifulSoup(session.get(FinalURl, headers = headers).content,'html.parser')
    if moviesoup.find_all('div',{'class':'i3LlFf'}):
        FinalSP=[x.get_text() for x in moviesoup.find_all('div',{'class':'i3LlFf'})]
        print("Movie Name:{0} and you Could watch on {1}".format("\033[1m"+li+"\033[0;0m","\033[1m"+str(FinalSP)[1:-1])+"\033[0;0m")
    else:
        print("Movie Name:{0} and you Could watch on {1}".format("\033[1m"+li+"\033[0;0m","\033[1m"+"'NA'"+"\033[0;0m"))