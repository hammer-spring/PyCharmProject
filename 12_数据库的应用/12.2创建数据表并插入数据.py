import sqlite3

conn = sqlite3.connect('D:/PyCharm/PyCharmProject/12_数据库的应用/person.db')
curs = conn.cursor()

curs.execute('''
CREATE TABLE person (
  id         TEXT       PRIMARY KEY,
  name       TEXT,
  age        INT,
  info       TEXT
  )
''')
curs.execute('''
INSERT INTO person VALUES(
  1,'张芳',21,'舞者'
  )
''')
curs.execute('''
INSERT INTO person VALUES(
  2,'黄玉',28,'歌手'
  )
''')
curs.execute('''
INSERT INTO person VALUES(
  3,'刘菲',26,'作家'
  )
''')

conn.commit()
conn.close()
