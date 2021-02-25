# coding=utf-8
from Tkinter import *
import tkMessageBox
import MySQLdb
import os


#用于从数据库查询可登录用户名，默认为１个，后续改进可查询登录多个用户
# def start():
#     db=MySQLdb.connect(host="127.0.0.1",port=3306,user="root",passwd="root123",db="test",charset='utf8')
#     cursor=db.cursor()
#     sql="""select username from admin"""
#     cursor.execute(sql)
#     data = cursor.fetchone()
#     a=int(len(data)-1)
#     return data[a]
# name222=start()

#将来还可以添加指定数据库，ip,端口
class loginPage(object):
    def __init__(self, master, info='password manage system'):
        self.master = master
        self.mainlabel = Label(master, text=info, justify=CENTER)
        self.mainlabel.grid(row=0, columnspan=3)

        self.user = Label(master, text='username', borderwidth=2)
        self.user.grid(row=1, sticky=W)

        self.pwd = Label(master, text='password', borderwidth=2)
        self.pwd.grid(row=2, sticky=W)

        self.userEntry = Entry(master)
        self.userEntry.grid(row=1, column=1, columnspan=2)
        self.userEntry.focus_set()

        self.pwdEntry = Entry(master, show='*')
        self.pwdEntry.grid(row=2, column=1, columnspan=2)

        self.loginButton = Button(master, text='Login', borderwidth=2, command=self.login)
        self.loginButton.grid(row=3, column=1)

        self.quitButton = Button(master, text='quit', borderwidth=2, command=self.quit)
        self.quitButton.grid(row=3, column=2)

    def login(self):
        self.username = self.userEntry.get().strip()
        self.passwd = self.pwdEntry.get().strip()
        if len(self.username) == 0 or len(self.passwd) == 0:
        # if len(self.username) == 0 or len(self.passwd) == 0 or self.username != name222:
            tkMessageBox.showwarning('警告', '用户未授权')
            self.clear()
            self.userEntry.focus_set()
            return
        self.connect1()

    # 用于测试数据连接是否正常
    def connect1(self):
        try:
            db = MySQLdb.connect(host="127.0.0.1", port=3306, user=self.username, passwd=self.passwd, db="test", charset='utf8')
            cursor = db.cursor()
            cursor.execute("select version()")
            data = cursor.fetchone()
            print "database version :%s" % data
            db.close()
        except:
            print "数据库连接错误"
        self.mychaxun = chaxun(self.master)

    def clear(self):
        self.userEntry.delete(0, END)
        self.pwdEntry.delete(0, END)
    def quit(self):
        #退出并备份数据库到指定地方。
        backup = "mysqldump -uroot -proot123 test > /home/tony/test111"
        os.system(backup)


class chaxun(object):

    def __init__(self, master):

        self.mainPage = Toplevel(master)

        self.nameLabel = Label(self.mainPage, text='name:')
        self.nameLabel.grid()
        self.nameEntry = Entry(self.mainPage)
        self.nameEntry.grid(row=0, column=1)

        self.urlLabel = Label(self.mainPage, text='url:')
        self.urlLabel.grid(row=1, column=0)
        self.urlEntry = Entry(self.mainPage)
        self.urlEntry.grid(row=1, column=1)

        self.usernameLabel = Label(self.mainPage, text='username:')
        self.usernameLabel.grid(row=2, column=0)
        self.usernameEntry = Entry(self.mainPage)
        self.usernameEntry.grid(row=2, column=1)

        self.passwordLabel = Label(self.mainPage, text='password:')
        self.passwordLabel.grid(row=3, column=0)
        self.passwordEntry = Entry(self.mainPage)
        self.passwordEntry.grid(row=3, column=1)

        self.emailLabel = Label(self.mainPage, text='email:')
        self.emailLabel.grid(row=4, column=0)
        self.emailEntry = Entry(self.mainPage)
        self.emailEntry.grid(row=4,column=1)

        self.phoneLabel = Label(self.mainPage, text='phone:')
        self.phoneLabel.grid(row=5, column=0)
        self.phoneEntry = Entry(self.mainPage)
        self.phoneEntry.grid(row=5, column=1)


        self.sendButton = Button(self.mainPage, text='插入', command=self.insert2)
        self.sendButton.grid(row=6, column=0)

        self.newButton = Button(self.mainPage, text='查询', command=self.select2)
        self.newButton.grid(row=6, column=1)

    def getInfo(self):
        self.nameinfo= self.nameEntry.get().strip()
        self.urlInfo = self.urlEntry.get().strip()
        self.usernameinfo = self.usernameEntry.get().strip()
        self.passwordInfo = self.passwordEntry.get().strip()
        self.emailinfo = self.emailEntry.get().strip()
        self.phoneInfo = self.phoneEntry.get().strip()

    def insert2(self):
        # 用于检查数据是否连接正常
        def connect2():
            try:
                db = MySQLdb.connect(host="127.0.0.1", port=3306, user="root", passwd="root123", db="test",
                                     charset='utf8')
                cursor = db.cursor()
                cursor.execute("select version()")
                data = cursor.fetchone()
                db.close()
                return "200"
            except:
                return "404"

        ma = connect2()
        if ma == 200:
            db = MySQLdb.connect(host="127.0.0.1", port=3306, user="root", passwd="root123", db="test", charset='utf8')
            cursor = db.cursor()
            #这样获取不到输入的值
            #a = "self.nameinfo,self.urlInfo,self.usernameinfo,self.passwordInfo,self.emailinfo,self.phoneInfo"
            sql2 = """insert into t4 values(8888)"""
            try:
                cursor.execute(sql2)
                db.commit()
            except:
                db.rollback()
        else:
            return tkMessageBox.showinfo('提示', '数据连接错误')

    def select2(self):
        db = MySQLdb.connect(host="127.0.0.1", port=3306, user="root", passwd="root123", db="test", charset='utf8')
        cursor = db.cursor()
        sql = """select * from admin"""
        cursor.execute(sql)



if __name__ == '__main__':
    root = Tk()
    root.title('简易密码管理程序')

    myLogin = loginPage(root)

    # root.wait_window(myLogin.mySendMail.sendPage)
    mainloop()
