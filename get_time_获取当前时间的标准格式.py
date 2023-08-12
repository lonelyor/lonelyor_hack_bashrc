# author：lonelyor
# time：2019-06-13
# describe：获取当前时间的标准格式【年-月-日 时:分:秒】

import time

def time_now():
    time_now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    return time_now

# print(time_now())