# description: 把字符串进行hash加密
# author: lonelyor
# version: v0.1
# time: 2018-06-11


import hashlib

＃把你要加密的字符串写到passwd即可
passwd = '123456'
m = hashlib.md5(passwd.encode())
m.update(passwd.encode())
print(m.hexdigest())
