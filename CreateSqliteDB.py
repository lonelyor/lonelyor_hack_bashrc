# author: lonelyor
# time: 2018-06-11
# description: 在当前目录创建sqlite3数据库

import sqlite3
import os

def createdb():
    # 获取当前目录下的文件名(列表),若数据库文件不存在则创建
    dirFilename = os.listdir(os.getcwd())
    x = input('输入创建的数据库名（example.db）:')
    # 判断文件是否存在，若不存在则创建
    if x in dirFilename:
        print('文件已存在')
    else:
        conn = sqlite3.connect(x)
        conn.close()
        print('数据库创建成功！')
    return x

