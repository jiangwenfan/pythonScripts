#!/usr/bin/python3
#【1】复制多个程序，
#【】并且全部启动。
import sys
import os
import time
import subprocess

def dispose_logic():
    source_process=str(sys.argv[1])
    number=int(sys.argv[2])
    #print("[test:]"+source_process)
    ## 1 & |的也可以实现
    os.system("mkdir deal_with_result 2> test.log")
    size=os.path.getsize("test.log")
    if size == 0:
        print("工作目录创建成功！")
        os.system("rm -rf test.log")
    else:
        answer=str(input("检测到工作目录已经存在，是否覆盖? (yes or no)"))
        if answer == "yes":
            os.system("rm -rf deal_with_result test.log")
            os.system("mkdir deal_with_result")
            print("工作目录创建成功！")
        else:
            print("正在退出程序...")
            sys.exit()

    for i in range(number):
        new_name=str(i)+".py"
        global path
        path="./deal_with_result/"
        #print("[test:] "+path+new_name)
        os.system("cp "+source_process+" "+path+new_name) #cp t1.py ./deal_with_result/0.py
    show_info("dispose")
    text="if you need to start all process? a total of "+num2+" 个。input:(yes or no)"
    answer=str(input(text))#是否需要全部启动。
    if answer == "yes":
        print("[test:]starting all programs")
    else:
        print("[test:] 已经退出程序.")

    #print("[test:] target is "+str(number))
    #print("\n[test:] list is "+str(len(range(number))))

def calc_number():
    #os.system("ls -l") #[test:] 调用函数就可显示内容
    global aa
    aa = os.popen("ls -l "+path+" |wc -l")

def show_info(content):
    if content == "title":
        print("\nonly is linux")
        print("Welcome to use this processus! Let's GO ...\n")
        if len(sys.argv) != 3:
            print("用法:  ./create.py [需要复制的程序] [复制的个数]")
            print("举例: ./create.py   t1.py   20")
            sys.exit()
    elif content == "end":
        print("\nthank you use this processus! Good Bye!\n")
    elif content == "dispose":
        calc_number()
        global num2
        num2=str(int(aa.read())-1)
        #print(type(num2))
        print("create sucess! number is "+num2+" 个程序")
    else :
        print("process is error!")


show_info("title")
dispose_logic()
show_info("end")


