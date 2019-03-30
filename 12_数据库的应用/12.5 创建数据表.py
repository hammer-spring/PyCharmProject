import pymysql

# 打开数据库连接
db = pymysql.connect("localhost","root","4303299","person" )

# 使用 cursor() 方法创建一个游标对象 cursor
cursor = db.cursor()
# 定义SQL语句
sql = """CREATE TABLE student(
id  INT(10) NOT NULL UNIQUE,
name  CHAR(20) NOT NULL,
age INT,
sex CHAR(1))
"""
# 使用 execute() 方法执行 SQL 
cursor.execute(sql)

# 关闭数据库连接
db.close()
