import time, datetime

# 时间格式转换
now = time.localtime(int(time.time()))
now1 = time.strftime("%Y-%m-%d_%H:%M:%S", now)
# now2 = time.strftime("%Y%m%d%H%M%S", now)

result = """
author: lonelyor
time: %s
des: %s
""" % (now1,'Null')

print(result)
