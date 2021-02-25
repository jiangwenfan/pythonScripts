import socket
import time

webData = []
def main():
    tcpServerSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcpServerSocket.bind(("",5656))
    tcpServerSocket.listen(128)
    global webData
    while True:
        print("\n\nwait a new client:")
        newClientSocket,clientAddr = tcpServerSocket.accept()
        print("client info: %s"%str(clientAddr))
        
        while True:
            recvData = newClientSocket.recv(1024)
            recvLength = len(recvData.decode("utf-8"))
            #根据收到的数据包的大小判断是从哪里来的请求
            if recvLength > 120:  
                #web请求
                # 设置返回的头信息 header
                response_headers = "HTTP/1.1 200 OK\r\n" # 200 表示找到这个资源
                response_headers += "\r\n" # 空一行与body隔开
                # 设置内容body
                response_body = "<h1>receive data :<h1>\r\n" 
                #sumInfo = ""
                for i in range(len(webData)):
                    #sumInfo = sumInfo+"\r\n"+i
                    ip = webData[i]
                    response_body += "<h2> "+ip+" <h2>\r\n" 
                #response_body += "<h3>binlang!!!<h3>\r\n" 
        
                # 合并返回的response数据
                response = response_headers + response_body
                # 返回数据给浏览器
                newClientSocket.send(response.encode("utf-8"))   #转码utf-8并send数据到浏览器
                print("web is over!")
            else:
                #client send ip
                ipInfo = recvData.decode("utf-8")
                if len(webData) > 10:
                    #清空
                    webData.clear()
                    webData.append(ipInfo)
                else:
                    webData.append(ipInfo)
                    
                print("receive data: \n%s"%ipInfo)
    
            break
        newClientSocket.close()
        print("it is over!")
    tcpServerSocket.close()

if __name__ == "__main__":
    main()
