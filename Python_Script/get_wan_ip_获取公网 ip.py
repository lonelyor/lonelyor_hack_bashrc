# author: lonelyor
# time: 2018-06-11
# description: 获取外网 ip，通过 ip 查询网站获取,如果获取不到就表示网站挂了，届时换别的网站就行了。

# 获取 ip 的接口
'''
http://www.3322.org/dyndns/getip
http://whois.pconline.com.cn/ipJson.jsp
http://pv.sohu.com/cityjson
http://ip.360.cn/IPShare/info
https://www.taobao.com/help/getip.php

检测 ip 的正则表达式（未验证）：
((2[0-4]\d|25[0-5]|[01]?\d\d?)\.){3}(2[0-4]\d|25[0-5]|[01]?\d\d?)
或者
^((25[0-5]|2[0-4]\\d|[1]{1}\\d{1}\\d{1}|[1-9]{1}\\d{1}|\\d{1})($|(?!\\.$)\\.)){4}$
'''

import requests

url = 'https://www.taobao.com/help/getip.php'

header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3775.400 QQBrowser/10.6.4208.400'
}


def get_wan_ip():
    r = requests.get(url=url, headers=header)
    ip = r.text
    return ip

print(get_wan_ip())