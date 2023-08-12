import hashlib

ans = str(input("Please input you answer: ")).encode('utf-8')
flag = "flag{%s}" % hashlib.md5(ans).hexdigest()
print(flag)
