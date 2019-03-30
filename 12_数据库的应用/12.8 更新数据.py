import pymysql

# 打开数据库连接
db = pymysql.connect("localhost","root","4303299","person" )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()
# SQL 更新语句
sql = "UPDATE student SET age=age-1"
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 提交到数据库执行
   db.commit()
except:
   # 发生错误时回滚
   db.rollback()

# 关闭数据库连接
