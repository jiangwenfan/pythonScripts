import socket

def main():
    tcpSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    serverIp = "sick.pwall.icu"
    serverPort = 5656
    serverAddr = (serverIp,serverPort)
    tcpSocket.connect(serverAddr)
    
    send_data = "hello : xxxxxxxxoooooooo"
    tcpSocket.send(send_data.encode("utf-8"))
    
    tcpSocket.close()

if __name__ == "__main__":
    main()
