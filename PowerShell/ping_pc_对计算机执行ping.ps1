Get-CimInstance -Class Win32_PingStatus -Filter "Address='127.0.0.1'"

# 多个地址可以这样

'127.0.0.1','localhost','bing.com' |
  ForEach-Object -Process {
    Get-CimInstance -Class Win32_PingStatus -Filter ("Address='$_'") |
      Select-Object -Property Address,ResponseTime,StatusCode
  }

# 对内网整个网段进行 ping 操作，网段地址自行修改

1..254| ForEach-Object -Process {
  Get-CimInstance -Class Win32_PingStatus -Filter ("Address='192.168.1.$_'") } |
    Select-Object -Property Address,ResponseTime,StatusCode