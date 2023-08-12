# author：lonelyor
# time：2019-06-13
# description：以顺序列表的形式返回指定长度的数字集

def passwd_char():
    passwd_length = int(input("密码长度："))
    passwd_max = int(passwd_length*'9')
    passwd_min = int('1'+(passwd_length-1)*'0')

    l = []
    for i in range(passwd_min, passwd_max):
        l.append(i)

    return l

passwd_char()