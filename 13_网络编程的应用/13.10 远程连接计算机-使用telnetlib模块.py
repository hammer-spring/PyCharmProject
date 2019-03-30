import telnetlib

#指定Telnet服务器
host = "http://www.dummy.com"

#指定用户帐号
username = "johnny" + "\n"
#指定用户密码
password = "123456" + "\n"

#创建Telnet类的实例变量
telnet = telnetlib.Telnet(host)

#登入Telnet服务器,输入用户帐号与密码
telnet.read_until("login: ")
telnet.write(username)
telnet.read_until("Password: ")
telnet.write(password)

#输入命令
while 1:
    command = raw_input("[shell]: ")
    telnet.write(command)
    if command == "exit":
        break
    telnet.read_all()
