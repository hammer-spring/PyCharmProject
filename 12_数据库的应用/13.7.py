import pymysql

# 打开数据库连接
db = pymysql.connect("localhost","root","","person" )

# 使用cursor()方法获取操作游标 
cursor = db.cursor()
sql = "SELECT * FROM student WHERE age > '%d'" % (25)
#执行SQL查询语句
try:
   # 执行SQL语句
   cursor.execute(sql)
   # 获取所有记录列表
   results = cursor.fetchall()
   for row in results:
      id = row[0]
      name = row[1]
      age = row[2]
      sex = row[3]
       # 打印结果
      print ("id=%s,name=%s,age=%d,sex=%s " % (id,name, age, sex))
except:
   print ("错误: 无法查询数据")

# 关闭数据库连接
db.close()
