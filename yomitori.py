import urllib.request
from bs4 import BeautifulSoup

url = 'https://search.yahoo.co.jp/realtime'
ua = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) '\
    'AppleWebKit/537.36 (KHTML, like Gecko) '\
    'Chrome/81.0.4044.138 Safari/537.36 '

req = urllib.request.Request(url, headers={'User-Agent': ua})
html = urllib.request.urlopen(req)
soup = BeautifulSoup(html, "html.parser")

topicsindex = soup.find('section', attrs={'class': 'contents'})
topics = topicsindex.find_all('li')

for topic in topics:
    print(topic.find('a').contents[0])