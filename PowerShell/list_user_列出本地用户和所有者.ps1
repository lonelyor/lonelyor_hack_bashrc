Get-CimInstance -ClassName Win32_OperatingSystem | Select-Object -Property BuildNumber,BuildType,OSType,ServicePackMajorVersion,ServicePackMinorVersion

# 或者

Get-CimInstance -ClassName Win32_OperatingSystem | Select-Object -Property *user*