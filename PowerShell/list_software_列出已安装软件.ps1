Get-ChildItem -Path $UninstallPath |
    ForEach-Object -Process { $_.GetValue('DisplayName') } |
    Sort-Object

# 包含软件版本的输出

Get-ChildItem $UninstallPath |
    ForEach-Object {
        $ProdID = ($_.Name -split '\\')[-1]
        Get-ItemProperty -Path "$UninstallPath\$ProdID" -ea SilentlyContinue |
        Select-Object -Property DisplayName, InstallDate, @{n='ProdID'; e={$ProdID}}, Publisher, DisplayVersion
} | Select-Object -First 3