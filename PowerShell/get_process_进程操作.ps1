# 获取指定进程信息
Get-Process -Name ex*
# 获取空闲进程信息
Get-Process -id 0

# 停止指定进程
Stop-Process -Name xxx
# 停止无响应进程
Get-Process | Where-Object -FilterScript {$_.Responding -eq $false} | Stop-Process



