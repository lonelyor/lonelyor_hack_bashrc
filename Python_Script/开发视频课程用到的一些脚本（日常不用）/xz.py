# 用来输出写笔记时的元信息
import time, datetime
import uuid
import os

# 去除文件名的空格
chap1 = str(input('请输入课时名称: '))
chap2 = "".join(chap1.split())

# 时间格式转换
now = time.localtime(int(time.time()))
now1 = time.strftime("%Y-%m-%d %H:%M:%S", now)
now2 = time.strftime("%Y%m%d%H%M%S", now)

# 文章唯一编号
uid = uuid.uuid1().hex

# 创建笔记元数据
meta1 = '''# %s    

> Author: lonelyor\t
> Time: %s\t
> Code: %s\t
> Des: 闭门即是深山，读书随处净土。\t  

[TOC]


''' % (chap2,now1,uid)

print(meta1)

# 创建博客元数据
meta2 = '''    
> Author: lonelyor\t
> Time: %s\t
> Des:  
''' % (now1)

print(meta2)