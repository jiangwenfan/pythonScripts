这是一个自动同步Windows虚拟机时间的小工具。


1.作为服务同步时间:
创建一个windows开机启动服务。建议将服务放到PCI Configuration组里面。

eg:
    sc create "test111" binpath= "C:\autoSynchronizeTime.exe" displayname= "test1111time" group= "PCI Configuration" start= auto 

2.双击同步时间
但仅仅只是双击同步时间时，需要以管理员身份运行才能同步时间。
