from http.cookiejar import FileCookieJar
import os

cwd = os.getcwd()
print(str(cwd))
os.chdir(cwd)
for dir_name in open("~/Script/mdir.txt"):
    os.makedirs(dir_name.strip()+'/课件')
    os.makedirs(dir_name.strip()+'/附件')
    os.makedirs(dir_name.strip()+'/视频')
