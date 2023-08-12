# author: lonelyor
# time: 2018-06-11
# description: 可以用来分析nginx日志，如果是进行本地测试请用nano添加数据，不要使用vim等编辑器（因为这些编辑器添加数据的方式是：文件替换），正常的log是对文件进行追加，而不是替换。

#import time你可以用这个模块来给该程序定时
import subprocess
import requests
#import os充分发挥想象力来使用这个模块
#import re规则嘛，用这个可以更强


# 日志文件位置
logfile = "~/testlog.log"
print('监控的日志文件是: %s' % logfile)
# 实时读取日志
command='tail -f '+logfile
popen=subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
#监控log文件并获取新增的内容
while True:
    line=popen.stdout.readline().strip().decode('utf8')
    new_line = [line]
    #print(line)
    #这里可以添加规则来对new_line进行处理，比如：如果触发规则，则把new_line发送到指定的服务器
    payload_r = ['a.com', 'b.com']
    for i in new_line:
        for j in payload_r:
            if j == i:
                #url即服务器地址
                url = 'http://localsanic.com:8877'
                req_post = requests.post(url, json=i)
                if req_post.status_code == 200:
                    print(req_post.text)
                else:
                    print('服务器返回异常,请检查服务器状态.')
