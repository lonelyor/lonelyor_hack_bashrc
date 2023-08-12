# 获取服务
Get-Service -Name se*
# 获取远程计算机服务列表，xxx 可以是 ip 地址
Get-Service -ComputerName xxx

# 启动、停止、重启、暂停服务
Start-Service -Name spooler
Stop-Service -Name spooler
Restart-Service -Name spooler
Suspend-Service -Name spooler