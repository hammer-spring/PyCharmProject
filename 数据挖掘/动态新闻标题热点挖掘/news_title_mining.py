import jieba.posseg as pseg
import matplotlib.pyplot as plt
from os import path
import re
import requests
import time
from scipy.misc import imread
from wordcloud import WordCloud

def fetch_sina_news():
    # PATTERN = re.compile('.shtml" target="_blank">(.*?)</a><span>(.*?)</span></li>')
    PATTERN = re.compile('"title":(.*?),')
    # BASE_URL = "http://roll.news.sina.com.cn/news/gnxw/gdxw1/index_"
    BASE_URL = 'https://feed.mix.sina.com.cn/api/roll/get?pageid=153&lid=2509&k=&num=50&page=1&r=0.9215877395260672&callback=jQuery31109730869266614104_1541854588324&_=1541854588341'
    # MAX_PAGE_NUM = 10
    with open('subjects.txt', 'w', encoding='utf-8') as f:
        #for i in range(1, MAX_PAGE_NUM):
            #print('Downloading page #{}'.format(i))
            # r = requests.get(BASE_URL + str(i)+'.shtml')
            r = requests.get(BASE_URL)
            # r.encoding='gb2312'
            # data = r.text
            data = r.text.encode('utf-8').decode('unicode-escape')
            
            p = re.findall(PATTERN, data)
            
            for s in p:
                # f.write(s[0])
                f.write(s)
            # time.sleep(5)
    
def extract_words():
    with open('subjects.txt','r', encoding='utf-8') as f:
        news_subjects = f.readlines()
    
    stop_words = set(line.strip() for line in open('stopwords.txt', encoding='utf-8'))
    
    newslist = []
    
    for subject in news_subjects:
        if subject.isspace():
            continue
        
        # segment words line by line
        p = re.compile("n[a-z0-9]{0,2}")    # n, nr, ns, ... are the flags of nouns
        word_list = pseg.cut(subject)     
        for word, flag in word_list:
            if not word in stop_words and p.search(flag) != None:
                newslist.append(word)
    
    content = {}
    for item in newslist:
        content[item] = content.get(item, 0) + 1
    
    d = path.dirname(__file__)
    mask_image = imread(path.join(d, "mickey.png"))
    wordcloud = WordCloud(font_path='simhei.ttf', background_color="grey", mask=mask_image, max_words=10).generate_from_frequencies(content)
    # Display the generated image:
    plt.imshow(wordcloud)
    plt.axis("off")
    wordcloud.to_file('wordcloud.jpg')
    plt.show()
    
if __name__ == "__main__":
    fetch_sina_news()
    extract_words()
