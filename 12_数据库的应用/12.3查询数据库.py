import sqlite3, sys

conn = sqlite3.connect('D:/PyCharm/PyCharmProject/12_数据库的应用/person.db')
curs = conn.cursor()

curs.execute('''
SELECT * FROM person
WHERE name="张芳"
''')
names = [f[0] for f in curs.description]
for row in curs.fetchall():
    for pair in zip(names, row):
        print ('%s: %s' % pair)
