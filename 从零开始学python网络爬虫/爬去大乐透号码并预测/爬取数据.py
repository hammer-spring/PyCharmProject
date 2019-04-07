from bs4 import  BeautifulSoup  as bs
import requests
import os

def get_url():
    data_1 = []
    for i in range(1,91):
        url = 'http://www.lottery.gov.cn/historykj/history_'+ str(i) +'.jspx?_ltype=dlt'
        data  = requests.get(url).text
        data  = bs(data,'lxml')
        data = data.find('tbody').find_all('tr')
        for content in data:
            number = content.get_text().strip().replace('\r','').replace('\t','').replace('\n',' ')
            with open('data_recent.csv','a') as f:
                f.write(number+'\n')
    f.close()
if __name__ == '__main__':
    get_url()
