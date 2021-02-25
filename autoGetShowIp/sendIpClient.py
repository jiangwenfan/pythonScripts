#主要功能是发送邮件。 目的：开机就发送邮件。 py3
#C:\Users\Administrator\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup 
#自己把自己添加到启动文件夹中，只针对于win7，还是不行，必须登录才能自动发送，没有任何意义
#发送gmail邮箱有2分钟延迟
import smtplib
from email.header import Header
from email.mime.text import MIMEText
import socket 
import time

#-----------------发送到自己的服务器------------
ip = "sick.pwall.icu"
port = 5656

#-------------------发送到email--------------------
mail_host = "smtp.126.com"      
mail_user = "zhan2103208467@126.com"                  # 用户名
mail_pass = "beida660xiaofan"               # 授权密码
 
sender = 'zhan2103208467@126.com'    # 发件人邮箱(最好写全, 不然会失败)
receivers = ['technology198964@gmail.com'] 
 
 
def getIp():
    hostname = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    if ip == "127.0.0.1":
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(('8.8.8.8', 80))
            ip = s.getsockname()[0]
        finally:
            s.close()
        info = "hostname: " + hostname +"<===========>ip: "+ip
        return info
    else:
        info = "hostname: " + hostname +"<===========>ip: "+ip
        return info

content = getIp() #email content
title = 'virtual machine is started!'  #email title

def sendEmail():
 
    message = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码
    message['From'] = "{}".format(sender)
    message['To'] = ",".join(receivers)
    message['Subject'] = title
 
    try:
        smtpObj = smtplib.SMTP_SSL(mail_host, 465)  # 启用SSL发信, 端口一般是465
        smtpObj.login(mail_user, mail_pass)  # 登录验证
        smtpObj.sendmail(sender, receivers, message.as_string())  # 发送
        print("mail has been send successfully.")
    except smtplib.SMTPException as e:
        print(e)
 
def send_email2(SMTP_host, from_account, from_passwd, to_account, subject, content):
    email_client = smtplib.SMTP(SMTP_host)
    email_client.login(from_account, from_passwd)
    # create msg
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')  # subject
    msg['From'] = from_account
    msg['To'] = to_account
    email_client.sendmail(from_account, to_account, msg.as_string())
 
    email_client.quit()

def sendToServer(ip,port,info):
    """
        设置自己服务器的ip和端口。
    """
    tcpSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

    serverIp = ip
    serverPort = port
    serverAddr = (serverIp,serverPort)
    tcpSocket.connect(serverAddr)
    
    send_data = info
    tcpSocket.send(send_data.encode("utf-8"))
    
    tcpSocket.close()
    print("send is ok!")

 
if __name__ == '__main__':
    #sendEmail() #发送到邮箱
    #currentTime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
    currentTime = time.strftime("%H:%M:%S",time.localtime())
    info = currentTime+" <=========> "+getIp()
    sendToServer(ip,port,info) #发送到Server


    # receiver = '***'
    # send_email2(mail_host, mail_user, mail_pass, receiver, title, content)
