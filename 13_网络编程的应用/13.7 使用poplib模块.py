import poplib, string

#指定POP服务器
host = "saturn.seed.net.tw"

#创建一个POP3类的实例变量
myServer = poplib.POP3(host)

#返回POP3服务器送出的欢迎字符串
print (myServer.getwelcome())

#输入电子邮件的帐号
myServer.user("johnny")
#输入电子邮件的密码
myServer.pass_("123456")

#返回信息列表
r, items, octets = myServer.list()

#读取最后一个信息
msgid, size = string.split(items[-1])

#返回最后一个信息号码的内容
r, msg, octets = myServer.retr(msgid)
msg = string.join(msg, "\n")

#打印后一个信息号码的内容
print (msg)
