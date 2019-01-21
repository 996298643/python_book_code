from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError, URLError

def getTitle(url):
    try:
        html = urlopen(url)
    except (HTTPError,URLError):
        return None
    try:
         bsObj = BeautifulSoup(html.read(), "html.parser")
         title = bsObj.head.title
    except AttributeError:
        return None
    return title

title = getTitle("http://www.baidu.com")

if title is None:
    print("没有title")
else:
    print(title)

    
