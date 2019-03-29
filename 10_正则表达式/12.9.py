import re

#打开文件
fileContent = open("D:\\python\\ch12\\12.1.html").read()

#设置正则表达式(regular expression)为http:...的类型
pattern = re.compile(r"(http://[\w-]+(?:\.[\w-]+)*(?:/[\w-]*)*(?:\.[\w-]*)*)")

#寻找文件内所有匹配正则表达式的字符串
re.findall(pattern, fileContent)

#将匹配正则表达式字符串,以超级链接类型的新字符串取代
result = re.sub(pattern, r"<a href=\1>\1</a>", fileContent)

#打开新文件
file = open("D:\\python\\ch12\\new.html", "w")

#写入新的HTML文件
file.write(result)
file.close()
