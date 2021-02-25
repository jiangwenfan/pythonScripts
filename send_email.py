#主要功能是发送邮件。
import smtplib
from email.header import Header
from email.mime.text import MIMEText

def sendEmail(info):
    mail_host = "smtp.126.com"      
    mail_user = "zhan2103208467@126.com"                  # 用户名
    mail_pass = "beida660xiaofan"               # 授权密码
    sender = 'zhan2103208467@126.com'    # 发件人邮箱
    receivers = ['zhan2103208467@163.com'] #接受邮箱 
    showinfo = "\t\t ip地址是: \n"+info
    content = 'server已经正常启动。。。'+"\n\n\n"+showinfo
    title = '程序自动发送。。'  
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
 
