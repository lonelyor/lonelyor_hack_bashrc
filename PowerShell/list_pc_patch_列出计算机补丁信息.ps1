Get-CimInstance -ClassName Win32_QuickFixEngineering -Property HotFixId | Select-Object -Property HotFixId

# 若要更详细（包含安装用户和时间）信息，使用以下命令
Get-CimInstance -ClassName Win32_QuickFixEngineering