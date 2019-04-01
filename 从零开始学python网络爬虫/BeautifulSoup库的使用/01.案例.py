from bs4 import BeautifulSoup
import requests
import time

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
}
res = requests.get('http://bj.xiaozhu.com/',headers=headers)
soup = BeautifulSoup(res.text,'html.parser')
print(soup.prettify())