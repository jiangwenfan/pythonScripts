#这是一个查看apt源同步进度的小脚本
import os
import time

while True:

    os.system("df -h |grep /dev/sda5 > info.txt")
    origin = 25
    with open("/home/jiang/info.txt") as f:

        a=f.read().strip()
        blist=a.split()
        used=blist[2][0:3]
        res = int(used)-origin
        #meifeng = /60
        baifen = (res/134)*100
        baifen = round(baifen,1)
        print("\n\n"+str(baifen)+"%\n\n")

        time.sleep(60)

