# author: lonelyor
# time: 2018-06-11
# description: 获取本地局域网ip地址（通过对本地网卡发送udp的方式获取）

import socket
def get_host_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()
    return ip
IP = get_host_ip()
print(IP)
