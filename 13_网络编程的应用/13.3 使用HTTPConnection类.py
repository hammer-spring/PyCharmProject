import http.client

#指定主机名称
url = "www.xinhuanet.com"
#指定打开的文件名称
urlfile = "/fortune.html"

#连接到主机
host = http.client.HTTPConnection (url)

#写入客户端要求表头的第一行
host.request("GET", urlfile)
#获取服务器的响应
r1=host.getresponse()
#打印服务器返回的状态
print(r1.status,r1.reason)
#将file对象的内容存入新文件
file = open("D:\\PyCharm\\PyCharmProject\\13_网络编程的应用\\13.1.html", "w")
#读取网页内容,以utf-8方式保存
str = r1.read().decode("utf-8")
#寻找文本
print(str.find("mlive")) 
#写到文件并替换 'xa0' 为空字符
file.write(str.replace('\xa0','')) 
#关闭文件
file.close()
