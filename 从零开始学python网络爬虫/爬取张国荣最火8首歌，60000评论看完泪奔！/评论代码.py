# coding:utf-8import json
import time
import requests
from fake_useragent import UserAgent
import random
import multiprocessing
import sys
#reload(sys)#sys.setdefaultencoding('utf-8')

ua = UserAgent(verify_ssl=False)

song_list = [{'186453':'春夏秋冬'},{'188204':'沉默是金'},{'188175':'倩女幽魂'},{'188489':'风继续吹'},{'187374':'我'},{'186760':'风雨起时'}]
headers = {
    'Origin':'https://music.163.com',
    'Referer': 'https://music.163.com/song?id=26620756',
    'Host': 'music.163.com',
    'User-Agent': ua.random
}

def get_comments(page,ite):
    # 获取评论信息
    # """
    for key, values in ite.items():
        song_id = key
        song_name = values
    ip_list = [IP列表]
    url = 'http://music.163.com/api/v1/resource/comments/R_SO_4_'+ song_id +'?limit=20&offset=' + str(page)
    proxies = get_random_ip(ip_list)
    try:
        response = requests.get(url=url, headers=headers,proxies=proxies)
    except Exception as e:
        print (page)
        print (ite)
        return 0
    result = json.loads(response.text)
    items = result['comments']
    for item in items:
        # 用户名
        user_name = item['user']['nickname'].replace(',', '，')
        # 用户ID
        user_id = str(item['user']['userId'])
        print(user_id)
        # 评论内容
        comment = item['content'].strip().replace('\n', '').replace(',', '，')
        # 评论ID
        comment_id = str(item['commentId'])
        # 评论点赞数
        praise = str(item['likedCount'])
        # 评论时间
        date = time.localtime(int(str(item['time'])[:10]))
        date = time.strftime("%Y-%m-%d %H:%M:%S", date)