import pymysql

# 打开数据库连接
db = pymysql.connect("localhost","root","","person" )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()
sql = "INSERT INTO student (id,name,age,sex)VALUES ('%d', '%s', '%d', '%s' )" % (1, '张芳', 26, '女')
try:
   #执行插入数据语句
cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # 如果发生错误则回滚
   db.rollback()

# 关闭数据库连接
db.close()
