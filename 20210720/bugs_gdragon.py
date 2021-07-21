import urllib.request as req
from bs4 import BeautifulSoup
url='https://music.bugs.co.kr/chart'
soup=BeautifulSoup(req.urlopen(url),'html.parser')
res=soup.find_all('tr',{'rowtype':'track'}) # tags named tr with one of its attribute, rowtype, is track
titles=[]
for i in res:
    titles.append(i.find('input',{'name':'check'})['title']) # a tag named input with one of its attribute, name, is check
print(titles)

