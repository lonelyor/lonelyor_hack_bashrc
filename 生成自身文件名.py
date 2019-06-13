# author：lonelyor
# time：2019-06-13
# description：获取脚本自己的文件名，然后打印出来。

import os

def oneself_filename():
    oneself_name = os.path.basename(__file__)
    return oneself_name

print(oneself_filename())