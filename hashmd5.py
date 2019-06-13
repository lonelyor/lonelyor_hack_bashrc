# author: lonelyor
# time: 2018-06-11
# description: 把字符串进行hash加密


import hashlib

# 把你要加密的字符串写到passwd即可
passwd = str(input('请输入要加密的字符串：'))
m = hashlib.md5(passwd.encode())
m.update(passwd.encode())
print(m.hexdigest())
