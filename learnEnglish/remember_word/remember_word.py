#这是一个记单词的小程序，输入word.txt单词或句子文件，输出当前时间.txt文件。

import os
import time

filelist = []
t = time.localtime()
year = t.tm_year
mon = t.tm_mon
day = t.tm_mday

def show():
    os.system("clear")
def readfile(FileName):
    with open(FileName) as f:
        for i in f:
            a = i.split(',') 
            filelist.append(a)
        
def readlist():
    length = len(filelist)
    for j in range(length):
        en = filelist[j][0]
        cn = filelist[j][1].strip("\n")
        show()
        enter = "\n\n\n\n\n"*2
        #message = input(enter+en+" : ")
        cmd = "\033[1;32;40m"+en+" : "+"\033[0m"
        message = input(enter+cmd)
        txt = en+","+cn+"  :"+message+"\n"+"\n"
        filename = str(year)+"_"+str(mon)+"_"+str(day)+".txt"
        with open(filename,'a') as f:
            f.write(txt)
    print("\n\n\n\n\n")
 
def main():
    readfile('word.txt')
    readlist()

if __name__ == '__main__':
    main()
