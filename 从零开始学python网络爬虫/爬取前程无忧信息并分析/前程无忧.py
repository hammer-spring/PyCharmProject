# -*- coding: utf-8 -*-
'''
获取前程无忧python相关工作地点、薪水、公司、职位
'''

import requests
from bs4 import BeautifulSoup
headers={
        'UserAgent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
        }
total=[]
for i in range(1,21):
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
    for post,comp,area,money in zip(post1,comp1,area1,money1):
        total.append({'post':post,'comp':comp,'area':area,'money':money})#打包成字典
print(total)

import pandas
deal=pandas.DataFrame(total)
#print(deal)

deal.to_excel('qianchengwuyou.xls')

#以下从excel中提取数据，进行分析
import pandas as pd
a=pd.read_excel('qianchengwuyou.xls')
#筛选出有万和月的
b=[]
aa=a['money'].dropna()
for i in aa:
    if '月' in i and type(i)==str:
        if '万' in i:
            b.append(i)
#print(b)

import re
#字符串分割
d=[]
for c in b:
    d.append(re.split('[-/]',c))
#print(d)
#最小值组成列表
min=[]
for e in d:
    min.append(e[0])
#print(min)
#最小值以千为单位
gg=[]
for ff in min:
    if len(ff)==1:
        ff=ff+'0'
    else:
        ff=ff.replace('.','')
        gg.append(ff)
#print(gg)
#min求和
kk=0
for hh in gg:
    kk=kk+int(hh)
print(kk)
#所有min平均值
ever=kk/len(gg)
print(ever)

#最大值组成列表
max=list(map(lambda x:x[1].strip('万'),d))
#print(max)
#最大值以千为单位
g=[]
for f in max:
    if len(f)==1:
        f=f+'0'
    else:
        f=f.replace('.','')
        g.append(f)
#print(g)
#max求和
k=0
for h in g:
    k=k+int(h)
print(k)
#所有max平均值
eve=k/len(g)
print(eve)


import pandas
ik=list(map(int ,g))
ik1=pandas.Series(ik)



import matplotlib.pyplot as plt
#概率分布直方图
#高斯分布
#均值为0
"""  
mean = 100 
#标准差为1，反应数据集中还是分散的值  
sigma = 1  
x=mean+sigma*np.random.randn(10000) 
"""
plt.rcParams['font.sans-serif']=['SimHei']
fig,(ax0,ax1) = plt.subplots(nrows=2,figsize=(9,6))
#第二个参数是柱子宽一些还是窄一些，越大越窄越密
ax0.hist(ik,20,normed=1,histtype='bar',facecolor='yellowgreen',alpha=0.75)
##pdf概率分布图，一万个数落在某个区间内的数有多少个
ax0.set_title('基于前程无忧数据的python开发薪水调查')
ax1.hist(ik1,normed=100,histtype='bar',facecolor='pink',alpha=0.75,cumulative=True,rwidth=0.8)
#cdf累计概率函数，cumulative累计。比如需要统计小于5的数的概率
ax1.set_title("cdf")
fig.subplots_adjust(hspace=0.4)
plt.show()

