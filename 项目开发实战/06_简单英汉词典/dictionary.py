# -*- coding: utf-8 -*-

import re
import urllib
from urllib.request import urlopen
import urllib.parse
from tkinter import *

class Youdao:
    def __init__(self):
        # 有道翻译的释义所在的标签
        self.trans_tag_youdao = re.compile(r'\s?<li>.*?</li>\s?')

    # 爬虫需要的 url
    def getUrl(self):
        word = entry_word.get().replace(' ', '')
        if urllib.parse.quote(word) == word:
            search_url = "http://dict.youdao.com/w/" + urllib.parse.quote(word) + "/#keyfrom=dict2.top"
            return search_url

    # 爬取给定 url 的页面
    def getPage(self):
        search_url_youdao = self.getUrl()
        # 浏览器请求
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
        headers = {'User-Agent': user_agent}
        req = urllib.request.Request(search_url_youdao, headers=headers)
        response = urllib.request.urlopen(req)
        # 将其他编码的字符串转换成 unicode 编码
        the_page = response.read().decode("utf-8")
        return the_page

    # 提取网页中所需要的信息
    def extractPage(self):
        paraphrase = ""
        # 获取页面
        page = self.getPage()

        # 获取有道的基本翻译
        trans_youdao = self.trans_tag_youdao
        paraphrase += "有道词典翻译: \n"
        paraphrase += "\n"
        # 获取标签之间的所有内容（包含释义）
        items = re.findall('<div.*?class="trans-container">(.*?)<div id="webTrans" class="trans-wrapper trans-tab">', page, re.S)

        for item in items:
            youdao_tmp = item
            trans_iterator_youdao = trans_youdao.finditer(youdao_tmp)
            for iterator in trans_iterator_youdao:
                tag_paraphrase = iterator.group()
                tag_youdao = re.compile('\s?<.*?>')
                paraphrase += tag_youdao.sub('', tag_paraphrase) + '\n'
        paraphrase += "\n"
        return paraphrase

    # 获得查询单词，调用 extracPage( ) 函数，获得释义，将释义传给窗口变量
    def getParaphrase(self):
        en_ch = entry_word.get().replace(' ', '')
        if en_ch == '':
            strs = "请输入您要查询的单词！"
            text_paraphrase.set(strs)
        elif en_ch.isalpha() or en_ch.isdigit():
            paraphrase = self.extractPage()
            if paraphrase == "" or paraphrase == "有道词典翻译: \n" + '\n' + '\n':
                strs = "没有发现该单词——%s的释义！" % en_ch
                text_paraphrase.set(strs)
            else:
                text_paraphrase.set(paraphrase)
        else:
            strs = "您的输入有误，请重新输入您要查询的单词！"
            text_paraphrase.set(strs)

if __name__ == '__main__':
    mydict = Youdao()

    # 绘制窗口，并分配小部件位置，同时设置各部件参数
    root = Tk()
    root.title('英汉词典')
    root.geometry('800x600')
    label_word = Label(root, text="查询:", font=("Helvetica", 16), width=8, height=3)
    entry_word = Entry(root, font=("Helvetica", 16), width=50)
    label_paraphrase = Label(root, text="释义:", font=("Helvetica", 16), width=8, height=3)
    text_paraphrase = StringVar()
    out_paraphrase = Label(root, textvariable=text_paraphrase, font=("Helvetica", 16), bg='white', width=50, height=17, wraplength=550, justify='left')
    label_word.grid(row=0, column=0)
    entry_word.grid(row=0, column=1)
    label_paraphrase.grid(row=1, column=0)
    out_paraphrase.grid(row=1, column=1)
    label_empty = Label(root, text="", font=("Helvetica", 16), width=1, height=1)
    label_empty.grid(row=2, column=0)
    btn_query = Button(root, text="查询", command=mydict.getParaphrase, font=("Helvetica", 16), width=10, height=1)
    btn_query.grid(row=3, column=1)
    root.mainloop()