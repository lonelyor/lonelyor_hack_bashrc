# author：lonelyor
# time：2019-06-13
# description：获取 13 位 unix 时间戳

import time

def unix_time():
    now = int(time.time()*1000)
    return now

# print(unix_time())