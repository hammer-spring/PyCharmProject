# 引入 CGI 处理模块 
import cgi, cgitb 

# 创建 FieldStorage的实例 
form = cgi.FieldStorage() 

# 接收字段数据
if form.getvalue('java'):
   java_flag = "是"
else:
   java_flag = "否"

if form.getvalue('python'):
   python_flag = "是"
else:
   python_flag = "否"

print ("Content-type:text/html")
print()
print ("<html>")
print ("<head>")
print ("<meta charset=\"utf-8\">")
print ("<title>接收复选框中的数据</title>")
print ("</head>")
print ("<body>")
print ("<h2>Python语言是否被选择: %s</h2>" % python_flag)
print ("<h2> Java语言是否被选择: %s</h2>" % java_flag)
print ("</body>")
print ("</html>")
