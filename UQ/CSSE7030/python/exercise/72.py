import requests
from bs4 import BeautifulSoup
import pprint
import json


r=requests.get('https://maoyan.com/board/4')
r.encoding='utf-8'
print(r.text)

#soup=BeautifulSoup(html,'html.parser')












