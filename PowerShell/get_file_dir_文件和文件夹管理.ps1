# 列出某文件夹内所有目录
Get-ChildItem -Path C:\ -Force
# 列出某文件夹内所有目录和子目录
Get-ChildItem -Path C:\ -Force -Recurse

# 复制 boot.ini 到 boot.bak，强制覆盖则添加 -Force 参数
Copy-Item -Path C:\boot.ini -Destination C:\boot.bak

# 创建文件和文件夹
New-Item -Path 'C:\temp\New Folder' -ItemType Directory
New-Item -Path 'C:\temp\New Folder\file.txt' -ItemType File

# 删除某目录内所有内容
Remove-Item -Path C:\temp\DeleteMe -Recurse

# 使用通配符列举文件
# 查找带有后缀 .log 并且基名称中正好有五个字符的所有文件
Get-ChildItem -Path C:\Windows\?????.log
# 以 x 开头的目录
Get-ChildItem -Path C:\Windows\x*
# 以 x 开头的文件
Get-ChildItem -Path C:\Windows\[x]*
# 以 x 或 z 开头的文件
Get-ChildItem -Path C:\Windows\[xz]*

