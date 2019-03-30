import nntplib
import string

#指定NNTP服务器
host = "news.microsoft.com"

#指定新闻群组
group = "microsoft.public.java.activex"

#输入要搜索的关键词
keyword = raw_input("Enter keyword to search: ")

#连结到NNTP服务器
myServer = nntplib.NNTP(host)

#送出一个"GROUP"命令
r, count, first, last, name = myServer.group(group)

#返回所有的新闻稿
r, messages = myServer.xover(first, last)

#读取新闻稿的内容
for id, subject, author, date, msgid, refer, size, lines in messages:
    
    #找到新闻稿中的主题有要搜索的关键词
    if string.find(subject, keyword) >= 0:

        #读取id号码的新闻稿
        r, id, msgid, msgbody = myServer.article(id)

        #打印该新闻稿的作者,主题,与日期
        print ("Author: %s - Subject: %s - Date: %s\n" % (author, subject, date))

        #打印该新闻稿的内容
        print ("<-Begin Message->\n")
        print (msgbody)
        print ("<-End Message->\n")
