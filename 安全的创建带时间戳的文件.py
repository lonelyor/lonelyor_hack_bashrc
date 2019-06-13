# author：lonelyor
# time：2019-06-13
# description：创建文件前会进行判断，如果文件已存在则不创建，不存在则创建，不过带有 unix 时间戳的文件，存在同名文件的情况几乎不可能。

import time
import os

def creat_file():
    filename = str(input('请输入文件名：'))
    filesuf = str(input('输入文件后缀：'))
    now = str(int(time.time()*1000))

    files = filename + '_' + now + '.' + filesuf

    if not os.path.exists(files):
        with open(files, 'w'):
            print('success')
            pass
    else:
        print('file already exists')
        pass

creat_file()
