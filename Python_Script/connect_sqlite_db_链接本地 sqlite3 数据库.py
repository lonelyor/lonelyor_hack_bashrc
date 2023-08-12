# author: lonelyor
# time: 2018-06-11
# description: 连接sqlite3数据库，然后执行（查询）操作

import sqlite3

#sqlite.db文件的位置
sqlite3_db = '/home/lonelyor/document/xxx.db'
conn = sqlite3.connect(sqlite3_db)
print('连接成功')
cur = conn.cursor()
#查询语句
statement = 'SELECT xxxxxxxxxxxxxxxx'
cur.execute(statement)
res = cur.fetchall()
print(res)
