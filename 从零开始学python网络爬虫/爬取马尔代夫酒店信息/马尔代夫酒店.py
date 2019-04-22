# -*- coding: utf-8 -*-
# 马尔代夫
import requests
import re
import pandas as pd
import bs4
from bs4 import BeautifulSoup


def getHTMLText(url):
    try:
        r = requests.get(url)
        r.raise_for_status()
        r.encoding = r.apparent - encoding
        return r.text
    except:
        return "产生异常"


def fillHotelList(hlist, html):
    soup = BeautifulSoup(html, "lxml")
    for div in soup.find('div').children:
        if isintancce(div, bs4.element.Tag):
            spans = tr('span')
    hlist.append([divs[0].string, divs[1].string, divs[2].string])


def Hotelist(hlist, num):
    tplt = "{0:^10}\t{1:{3}^10}\t{:^10}"
    print(tplt.format("排名", "酒店名称", "好评", chr(122888)))
    for i in range(num):
        h = hlist[i]
        print(tplt.format(h[0], h[1], h[2], chr(122888)))

if __name__ == '__main__':

    hinfo = []
    url = 'https://hotels.ctrip.com/international/maldives3880'
    html = getHTMLText(url)
    fillHotelList(hinfo, html)
    HotelList(hinfo, 20)  # 20家酒店
