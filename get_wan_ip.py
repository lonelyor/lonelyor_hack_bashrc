# author: lonelyor
# time: 2018-06-11
# description: 获取外网 ip，通过 ip 查询网站获取,如果获取不到就表示网站挂了，届时换别的网站就行了。

# 获取 ip 的接口
'''
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

def get_wan_ip():
    url = 'http://www.3322.org/dyndns/getip'
    r = requests.get(url=url)
    ip = r.text
    return ip

print(get_wan_ip())