import uuid
import hashlib
import time, datetime
import pyperclip

uid = uuid.uuid4()
m = hashlib.md5()

# 时间格式转换
now = time.localtime(int(time.time()))
now1 = time.strftime("%Y-%m-%d %H:%M:%S", now)
# now2 = time.strftime("%Y%m%d%H%M%S", now)

m2 = str(uid)+str(now1)
m.update(m2.encode('utf-8'))
# 获取uuid与时间戳md5加密后的值
m5 = m.hexdigest()

result = """
title: %s
category: %s
tags: %s
des: %s
env: ["None"]
author: lonelyor
time: %s
code: %s
""" % ('空','空','空','空',now1,m5)

print(result)
