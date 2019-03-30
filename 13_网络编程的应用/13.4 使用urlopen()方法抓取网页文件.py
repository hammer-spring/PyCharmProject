import urllib.request
#打开网页文件
htmlhandler = urllib.request.urlopen("http://www.runoob.com")

#在本机上创建一个新文件
file = open("D:\\PyCharm\\PyCharmProject\\13_网络编程的应用\\13.2.html", "wb")

#将网页文件存储到本机文件上,每次读取512个字节
while 1:
    data = htmlhandler.read(512)
    if not data:
        break
    file.write(data)

#关闭本机文件
file.close()
#关闭网页文件
htmlhandler.close()
