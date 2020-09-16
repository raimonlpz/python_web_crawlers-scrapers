from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import HTTPError
from urllib.error import URLError

# try:
#     html = urlopen('http://pythonscraping.com/pages/page1.html')
# except HTTPError as e:
#     print(e)
# except URLError as e:
#     print('The server could not be found!')
#     # return null, break, or de some other PLAN B
# else:
#     print('It worked...')
#     # program continues

# bs = BeautifulSoup(html.read(), 'lxml')
# print(bs.h1)


def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as _e:
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.body.h1
    except AttributeError as _e:
        return None
    return title


title = getTitle('http://www.pythonscraping.com/pages/page1.html')
if title == None:
    print('Title could not be found')
else:
    print(title)
