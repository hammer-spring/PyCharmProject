import requests
from bs4 import BeautifulSoup
import re
import json
import time
import random
import os

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3355.4 Safari/537.36',
    'Referer': 'http://music.163.com',
    'Host': 'music.163.com'
}


# 获取页面源码
def GetHtml(url):
    try:
        res = requests.get(url=url, headers=headers)
    except:
        return None
    return res.text


# 提取歌手歌词信息
def GetSongsInfo(url):
    print('[INFO]:Getting Songs Info...')
    html = GetHtml(url)
    soup = BeautifulSoup(html, 'lxml')
    links = soup.find('ul', class_='f-hide').find_all('a')
    if len(links) < 1:
        print('[Warning]:_GetSongsInfo <links> not find...')
    Info = {'ID': [], 'NAME': []}
    for link in links:
        SongID = link.get('href').split('=')[-1]
        SongName = link.get_text()
        Info['ID'].append(SongID)
        Info['NAME'].append(SongName)
    # print(Info)
    return Info


def GetLyrics(SongID):
    print('[INFO]:Getting %s lyric...' % SongID)
    ApiUrl = 'http://music.163.com/api/song/lyric?id={}&lv=1&kv=1&tv=-1'.format(SongID)
    html = GetHtml(ApiUrl)
    html_json = json.loads(html)
    temp = html_json['lrc']['lyric']
    rule = re.compile(r'\[.*\]')
    lyric = re.sub(rule, '', temp).strip()
    print(lyric)
    return lyric


def main():
    SingerId = input('Enter the Singer ID:')
    url = 'http://music.163.com/artist?id={}'.format(SingerId)
    # url = "http://music.163.com/artist?id=6457"
    Info = GetSongsInfo(url)
    IDs = Info['ID']
    i = 0
    for ID in IDs:
        lyric = GetLyrics(ID)
        SaveLyrics(Info['NAME'][i], lyric)
        i += 1
        time.sleep(random.random() * 3)
        # print('[INFO]:All Done...')


def SaveLyrics(SongName, lyric):
    print('[INFO]: Start to Save {}...'.format(SongName))
    if not os.path.isdir('./results'):
        os.makedirs('./results')
    with open('./results/{}.txt'.format(SongName), 'w', encoding='utf-8') as f:
        f.write(lyric)