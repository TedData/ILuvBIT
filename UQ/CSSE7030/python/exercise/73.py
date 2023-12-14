import requests
#from bs4 import BeautifulSoup
#import pprint
import re
'''
head={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36 QQBrowser/4.4.106.400'}
r=requests.get('https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4',headers=head)
r.encoding='utf-8'
print(r.text)
regex='<a href="https://book.douban.com/subject/!\d+!/" title="!(.+?)!"'
data=re.findall(regex,r.text)
print(data)'''



head={'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36 QQBrowser/4.4.106.400'}

r=requests.get('https://movie.douban.com/chart',headers=head)
#r.encoding='utf-8'
print(r.text)
regex='<a class="nbg" href="https://movie.douban.com/subject/\d+/"  title="(.+?)"'


data=re.findall(regex,r.text)   
print(data)


'''
url='https://www.kaggle.com/datasets'
return_data=requests.get(url,headers=head).text #进行HTTP请求

print(return_data)

regex='<a href="/\d+" title="(.+?)" class="sc-pRcHn bdZJBZ"></a>'

#<trans oldtip="60k Stack Overflow Questions with Quality Rating" newtip="60k具有质量等级的堆叠溢出问题">60k Stack Overflow Questions with Quality Rating</trans>


data=re.findall(regex,return_data)
print(data)'''




