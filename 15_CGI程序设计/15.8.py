import re

#发生例外时的显示字符串
TemplateException = "Error while parsing HTML template"
#用来取代template1.html文件内的"<!-- # INSERT HERE # -->"字符串
content = "Hello Python"

#打开模板文件
filehandle = open("template1.html", "r")
#读取template文件的内容
data = filehandle.read()
#关闭template文件     
filehandle.close()

#将template1.html文件内的"<!-- # INSERT HERE # -->"字符串以content取代
matching = re.subn("<!-- # INSERT HERE # -->", content, data)

#发生错误
if matching[1] == 0:
    raise TemplateException

#成功,输出表头
print ("Content-Type: text/html\n\n")

#输出取代后的template1.html文件
print (matching[0])
