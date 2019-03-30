from ftplib import FTP

ftp = FTP()
timeout = 30
port = 21
# 连接FTP服务器
ftp.connect('192.168.1.106',port,timeout) 
# 登录FTP服务器
ftp.login('adminns','123456') 
# 获得欢迎信息
print (ftp.getwelcome())
ftp.cwd('file/test')    # 设置FTP路径
list = ftp.nlst()       # 获得目录列表
# 打印文件名字
for name in list:
    print(name) 
# 文件保存路径
path = 'd:/data/' + name 
# 打开要保存文件
f = open(path,'wb') 
# 保存FTP文件
filename = 'RETR ' + name   
# 保存FTP上的文件
ftp.retrbinary(filename,f.write) 
# 删除FTP文件
ftp.delete(name)            
# 上传FTP文件
ftp.storbinary('STOR '+filename, open(path, 'rb')) 
# 退出FTP服务器
ftp.quit()                 
