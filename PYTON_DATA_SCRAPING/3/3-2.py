from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.baidu.com")
bsObj =  BeautifulSoup(html.read(), "html.parser")

for label in bsObj.findAll("",{"class":"s-news-rank-wrapper"}) :
    print(label[0].gettext())