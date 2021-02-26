echo off

echo "请确保程序在: C:\tools\ 文件夹中，才能使用此脚本一键创建"
echo "使用管理员运行"

sc create "test111" binpath= "C:\tools\autoSynchronizeTime.exe" displayname= "Synctime" group= "PCI Configuration" start= auto
