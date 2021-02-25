这是一个通过客户端自动发送ip和主机信息到服务器上，通过Web的5656端口访问显示。

主要是为了解决kvm虚拟机不知道ip的问题。虚拟机通过桥接上网,物理网络中存在dhcp,所以基本上每次获得的IP都不一样，而且平时会连接不同的网络，
这个就是为了解决开机就能获取ip的问题。

1.server:
    screen -S abc
    python3 getIpServer.py #运行服务端
    ctrl +a +d #退出

2.虚拟机client:
    pyinstall -F sendIpClient.py #打包成exe
    pyinstal -F sendIpClient.py #打包成可执行脚本

    windows设置开机启动:
        
    centos设置开机启动：
        在/etc/rc.d/rc.local中添加启动命令,例如: ./opt/sendIpClient

3.展示界面:
    http://ip:5656

