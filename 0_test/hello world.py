# -*- coding: utf-8 -*-
"""
Created on Wed May 15 00:26:02 2019

@author: acer
"""

import requests
from lxml import etree
import re
import pymongo
import time

client = pymongo.MongoClient('localhost', 27017)
mydb = client['mydb']
guaziche = mydb['guaziche']

headers = {

    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36',
    'Cookie': 'uuid=e78377da-c2bb-43a4-c770-201d47073093; ganji_uuid=7258676803095927203408; lg=1; user_city_id=13; clueSourceCode=10103000312%2300; sessionid=571af757-6d75-4b6e-8c96-963b57bcb532; _gl_tracker=%7B%22ca_source%22%3A%22-%22%2C%22ca_name%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_id%22%3A%22-%22%2C%22ca_s%22%3A%22self%22%2C%22ca_n%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22sid%22%3A78143014117%7D; guazi_tracker_session_pageload_snapshot=%7B%22common%22%3A%7B%22line%22%3A%22c2c%22%2C%22platform%22%3A%22web%22%2C%22pagetype%22%3A%22intro%22%7D%2C%22trackings%22%3A%5B%7B%22guid%22%3A%22e78377da-c2bb-43a4-c770-201d47073093%22%2C%22userid%22%3A%22-%22%2C%22sessionid%22%3A%22571af757-6d75-4b6e-8c96-963b57bcb532%22%2C%22page%22%3A%22https%3A%2F%2Fwww.guazi.com%2Fsh%2Fintro%2F%22%2C%22referer%22%3A%22https%3A%2F%2Fwww.guazi.com%2Fsh%2F%22%2C%22referrer%22%3A%22https%3A%2F%2Fwww.guazi.com%2Fsh%2F%22%2C%22city%22%3A%22sh%22%2C%22landing%22%3A%220%22%2C%22ca_s%22%3A%22pz_baidu%22%2C%22ca_n%22%3A%22tbmkbturl%22%2C%22ca_medium%22%3A%22-%22%2C%22ca_term%22%3A%22-%22%2C%22ca_content%22%3A%22%22%2C%22ca_campaign%22%3A%22%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22scode%22%3A%2210103000312%22%2C%22keyword%22%3A%22-%22%2C%22ca_keywordid%22%3A%22-%22%2C%22ca_transid%22%3A%22%22%2C%22version%22%3A1%2C%22client_ab%22%3A%22-%22%2C%22os%22%3A%22Windows%2010%22%2C%22screen_resolution%22%3A%221536%20x%20864%22%2C%22view_port%22%3A%221519%20x%20722%22%2C%22is_native%22%3A%220%22%2C%22tracker_version%22%3A%221.6.11%22%2C%22clientTime%22%3A%221557931690675%22%2C%22tracking_type%22%3A%22pageload%22%2C%22pageid%22%3A%2205541362-8920-414e-bcd7-378b15504506%22%7D%5D%7D; financeCityDomain=sh; jr_from=homehead; jr_apply_platform=web; e78377da-c2bb-43a4-c770-201d47073093_views=1; 571af757-6d75-4b6e-8c96-963b57bcb532_views=1; Hm_lvt_e6e64ec34653ff98b12aab73ad895002=1557931695; Hm_lpvt_e6e64ec34653ff98b12aab73ad895002=1557931695; antipas=2D7D8RRZ90a5I9W026g57J294; cainfo=%7B%22ca_s%22%3A%22pz_baidu%22%2C%22ca_n%22%3A%22tbmkbturl%22%2C%22ca_medium%22%3A%22-%22%2C%22ca_term%22%3A%22-%22%2C%22ca_content%22%3A%22%22%2C%22ca_campaign%22%3A%22%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22scode%22%3A%2210103000312%22%2C%22keyword%22%3A%22-%22%2C%22ca_keywordid%22%3A%22-%22%2C%22ca_transid%22%3A%22%22%2C%22platform%22%3A%221%22%2C%22version%22%3A1%2C%22display_finance_flag%22%3A%22-%22%2C%22client_ab%22%3A%22-%22%2C%22guid%22%3A%22e78377da-c2bb-43a4-c770-201d47073093%22%2C%22sessionid%22%3A%22571af757-6d75-4b6e-8c96-963b57bcb532%22%2C%22ca_b%22%3A%22-%22%2C%22ca_a%22%3A%22-%22%7D; cityDomain=sh; preTime=%7B%22last%22%3A1557935446%2C%22this%22%3A1557309276%2C%22pre%22%3A1557309276%7D'
}


# 获取详情页面url
def get_detail_urls(url):
    # 2.获取页面内容
    try:
        res = requests.get(url, headers=headers)
        text = res.content.decode('utf-8')
        #print(text)
        # 3.解析网页
        html = etree.HTML(text)
        ul = html.xpath('//ul[@class="carlist clearfix js-top"]')[0]
        #print(ul)
        list = ul.xpath('./li')
        # print(list)
        detail_urls = []
        for li in list:
            detail_url = li.xpath('./a/@href')
            detail_url = 'https://www.guazi.com' + detail_url[0]
            # print(detail_url)
            detail_urls.append(detail_url)
    except IndexError:
        pass
        return detail_urls

    # https://www.guazi.com/wenzhou/1d0b59d6c5ebe951x.htm#fr_page=list&fr_pos=city&fr_no=0


# 解析详情页面内容
def parse_detail_url(url):
    res = requests.get(url, headers=headers)
    text = res.content.decode('utf-8')
    html = etree.HTML(text)
    # print(html)
    title = html.xpath('//div[@class="product-textbox"]/h2/text()')[0]
    title = title.replace(r'\r\n', '').strip()  # 取代空格、换行去除首尾的空格
    # print(title)
    info = html.xpath('//div[@class="product-textbox"]/ul//li/span/text()')
    # print(info)
    price = html.xpath('//div[@class="pricebox js-disprice"]/span/text()')[0]
    price = price.replace(r'\r\n', '').strip()
    # print(price)
    host = html.xpath('//div[@class="basic-infor js-basic-infor js-top"]/dl/dt/span/text()')[0]
    # print(host)
    # address = html.xpath('//div[@class="guazi-detail-baomai"]/div[3]/p/text()')
    # print(address)
    # insurance=re.findall('<td width="50%" class="td2">(.*?)</td>',html.text,re.S)
    # print(insurance)
    cardtime = info[0]
    km = info[1]
    displacement = info[2]
    speedbox = info[3]
    infos = {
        'title': title,
        'host': host,
        # 'address':address,
        'cardtime': cardtime,
        'km': km,
        'displacement': displacement,
        'speedbox': speedbox,
        'price': price,
    }
    # print(infos)
    guaziche.insert_one(infos)
    return infos


def main():
    # 1.目标url
    base_url = 'https://www.guazi.com/sh/buy/o{}/'
    for i in range(1, 15):
        url = base_url.format(i)
        detail_urls = get_detail_urls(url)
        # print(detail_urls)
        for detail_url in detail_urls:
            infos = parse_detail_url(detail_url)
        # 4.保存数据


if __name__ == '__main__':
    main()
