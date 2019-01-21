from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://www.csdn.net")
bsObj =  BeautifulSoup(html.read(), "html.parser")

for label in bsObj.findAll("a"):
    if "href" in label.attrs:
        print(label.attrs["href"])