#获取本地局域网的ip地址
import socket

def offlineIp():
    """
        通过主机名获取到ip. hosts文件不能有错误。
        return: ip
    """
    hostname = socket.gethostname() #get hostname
    ip = socket.gethostbyname(hostname) #get ip
    return ip

def onlineIp():
    """
        通过socks连接获取ip,需要联网
        return: ip
    """
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(('8.8.8.8', 80))
        ip = s.getsockname()[0]
    finally:
        s.close()

    return ip

if __name__ == '__main__':
    print("test: ")
    print("offline: "+offlineIp())
    print("online: "+onlineIp())
