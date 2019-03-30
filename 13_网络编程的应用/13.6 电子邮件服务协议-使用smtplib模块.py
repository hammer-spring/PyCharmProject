import smtplib

#指定SMTP服务器
host = "smtp.163.com"

#寄件者的电子邮件信箱
sender = " weilikui@163.com "

#收件者的电子邮件信箱
receipt = " weilikui@163.com "

#电子邮件的内容
msg = """
您好:
    这是一个测试的电子邮件
"""

#创建SMTP类的实例变量
myServer = smtplib.SMTP(host)

#寄出电子邮件
myServer.sendmail(sender, receipt, msg)

#关闭连接
myServer.quit()
