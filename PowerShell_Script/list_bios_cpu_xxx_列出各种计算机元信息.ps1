# bios 信息
Get-CimInstance -ClassName Win32_BIOS

# 处理器信息
Get-CimInstance -ClassName Win32_Processor | Select-Object -ExcludeProperty "CIM*"

# 计算机制造商和型号
Get-CimInstance -ClassName Win32_ComputerSystem