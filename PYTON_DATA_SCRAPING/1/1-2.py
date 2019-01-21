from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError

try: 
    html = urlopen("http://www.baidu.com")
    if html is None:
        print("url is not found")
    else:
        print("continue")
except HTTPError as e:
    print(e)
    
bsObj = BeautifulSoup(html.read(), "html.parser")
print(bsObj.p)
print(bsObj.html.body.p)
print(bsObj.body.p)
print(bsObj.html.p)
print(bsObj.html.p)

print(bsObj.head.title)