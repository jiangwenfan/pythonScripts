import os
#统计单词个数
#统计词频，，，，但是不能进行词频排序显示
wordslist=[]
counts = 0
number = {}
li={}
sum_number = 0

def count_word(file):
    with open(file) as fo:
        book=fo.read() #read str
        words=book.split() #words list
        for i in words:
            wordslist.append(i)
        num = len(words)
        number[file]=num
        global sum_number
        sum_number = sum_number+num
def count():
    filelist=os.listdir()
    for file in filelist:
        filename = file.split('.')
        if filename[1] == "txt":
            count_word(file)
            global counts
            counts = counts+1
def show():
    print("all file number is :"+str(counts))
    for key,value in number.items():
        print(key+":"+str(value))
    print("\nall word number is :"+str(sum_number))
    print("ciping is: \n")
    for key,value in li.items():
        print(key+":"+str(value))

def ciping():
    for j in wordslist:
        wordnum=wordslist.count(j)
        li[j]=wordnum
count()
ciping()
show()
