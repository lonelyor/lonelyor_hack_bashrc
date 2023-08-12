import time
import uuid
import os, sys, subprocess

# 去除课程名的空格
chap1 = str(input('[+] 请输入课时名称（不需要.md）: '))
chap2 = "".join(chap1.split())

# 创建目录
if not os.path.exists(chap2):
    #如果不存在则创建目录
    os.makedirs(chap2)
    # 创建同名子目录，根据 win 或 linux 可能需要修改 chap3 的斜杠
    chap3 = '%s/%s' % (chap2,chap2)
    os.makedirs(chap3)
    print(chap2+' 目录创建成功')
else:
    # 如果目录存在则不创建，并提示目录已存在
    print(chap2+' 目录已存在')
    os._exit(0)

# 创建课程
# 输出课程名和位置
os.chdir(chap2)
print('[+] 您创作的课程名为:%s,课件位置为:%s' % (chap2,os.getcwd()))
sfjx = input('[+] 默认为y，是否继续?（y/n）: ')
if sfjx == 'y' or sfjx == '':
    subcategory_list = ['Binary','Web','Experience','IoT','Mobile','uncategorized']
    while True:
        subcategory = str(input('[+] 请输入课程类别（Binary、Web、Experience、IoT、Mobile、uncategorized）: '))
        if subcategory in subcategory_list:
            subpe = str(input('[+] 默认为n，是否有poc、exp?（y/n）: '))
            if subpe !='y':
                subpe = 'n'
                break
            elif subpe == 'y':
                subpe == 'y'
                break            
        else:
            print('您的输入有误请重新输入')
            continue

    # 时间格式转换
    now = time.localtime(int(time.time()))
    now1 = time.strftime("%Y-%m-%d %H:%M:%S", now)
    now2 = time.strftime("%Y%m%d", now)

    # 格式化课时名
    uid = uuid.uuid4()
    chap4 = chap2+'-'+str(now2)+'-'+str(uid)+'.md'

    # 创建课时元数据，作者名用自己的
    meta = '''# %s

---
subcategory: %s
subpe: %s
author: lonelyor
time: %s
code: %s

---

''' % (chap2,subcategory,subpe,now1,uid)

    file = open(chap4, 'a', encoding='utf-8')
    file.write(meta)
    file.close()

    time.sleep(0.1)

    osplatform = sys.platform
    # windows
    if osplatform == 'win32':
        os.startfile(chap4)
    # linux
    elif osplatform == 'linux':
        subprocess.call(["xdg-open", chap4])
    # mac 
    elif osplatform == 'darwin':
        subprocess.call(["open", chap4])
    else:
        print('未能自动检测到您的操作系统版本，请手动编辑md文件。')

elif sfjx == 'n' or sfjx != 'y' or sfjx != '':
    os._exit(0)