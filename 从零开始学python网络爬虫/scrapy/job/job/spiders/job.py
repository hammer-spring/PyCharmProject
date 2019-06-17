# -*- coding: utf-8 -*-
'''
获取前程无忧python相关职位、公司名、工作地点、薪资、发布时间
'''
import scrapy
from scrapy.spiders import CrawlSpider
from scrapy.selector import Selector
from scrapy.http import Request
from ..items import JobItem

class job(CrawlSpider):
    name = 'job'
    import requests
    from bs4 import BeautifulSoup
    name = 'job'
    headers={
            'UserAgent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
            }
    total=[]
    for i in range(1,51):
        url='http://search.51job.com/list/070000%252C020000,000000,0000,00,9,99,Python,2,{}.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=1&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='.format(i)
        res=requests.get(url)
        res.encoding='gbk'
        #print(res.encoding)
        soup=BeautifulSoup(res.text,'html.parser')
        #print(soup)
        posts=soup.select('#resultList > div > p > span > a')
        #print(posts)
        post1=list(map(lambda x:x.text.strip(),posts))
        #print(post1)#获取职位名称
        comps=soup.select('#resultList > div > span.t2 > a')
        comp1=list(map(lambda x:x.text.strip(),comps))
        #print(comp1)#获取公司名称
        areas=soup.select('#resultList > div > span.t3')
        area1=list(map(lambda x:x.text.strip(),areas))
        #print(area1)#获取公司地点
        moneys=soup.select('#resultList > div > span.t4')
        money1=list(map(lambda x:x.text.strip(),moneys))
        #print(money1)#获取薪水
        times=soup.select('#resultList > div > span.t5')
        time1=list(map(lambda x:x.text.strip(),times))
        #print(time1)#获取发布时间
        for post,comp,area,money,time in zip(post1,comp1,area1,money1,time1):
            total.append({'职位名':post,'公司名':comp,'工作地点':area,'薪资':money,'发布时间':time})#打包成字典
    print(total)

    #链接mongodb数据库
    import pymongo
    client = pymongo.MongoClient('localhost',27017) #'192.168.0.65',27777
    db = client.cast
    test = db.qianchengwuyou6

    for i in total:
        test.save(i)#存储数据
    query={'area':'上海'}
    lt=test.count(query)
    pos=list(test.find(query))


