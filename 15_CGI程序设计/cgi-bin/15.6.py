# 引入 CGI 处理模块 
import cgi, cgitb 

# 创建 FieldStorage的实例 
form = cgi.FieldStorage() 

# 接收字段数据
if form.getvalue(' selectss '):
   selectss_value = form.getvalue(' selectss ')
else:
   selectss_value = "没有内容"

print ("Content-type:text/html")
print()
print ("<html>")
print ("<head>")
print ("<meta charset=\"utf-8\">")
print ("<title>接收菜单中的数据</title>")
print ("</head>")
print ("<body>")
print ("<h2> 选中的选项是：%s</h2>" % selectss_value)
print ("</body>")
print ("</html>")
