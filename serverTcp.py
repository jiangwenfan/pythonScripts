import socket

def main():
    tcpServerSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcpServerSocket.bind(("",5656))
    tcpServerSocket.listen(128)
    while True:
        print("wait a new client:")
        newClientSocket,clientAddr = tcpServerSocket.accept()
        print("accept info: %s"%str(clientAddr))
        
        while True:
            recvData = newClientSocket.recv(1024)
            print("client data: \n%s"%recvData.decode("utf-8"))
            #newClientSocket.send("recept is ok!".encode("utf-8"))
            if recvData:
                break
        
        newClientSocket.close()
        print("it is over!")
    tcpServerSocket.close()

if __name__ == "__main__":
    main()
