import cv2
from PIL import ImageFont, ImageDraw, Image
import numpy as np
import random

file="C:\\Users\\JWF\Desktop\\new2.txt"
textList = []
fontColor = [(248,248,255),(46,139,87),(255,69,0)] #字体颜色池

image = "C:\\Users\\JWF\\Desktop\\test.png"

def read2List(file):
    with open(file,'r',encoding="utf-8") as f:
        count = 0 #读取每行的次数
        for line in f:
            textDict = {}
            wordList = line.split(" ") #每个单词的设置信息
            length = len(wordList)
            if(length == 3):
                word0 = wordList[0]
                word1 = wordList[2]
                text = word0 +"  "+word1 #ant 蚂蚁 这里可以修改英文和汉语的间隔符
                #print(text)
                textDict["text"] = text 
                textDict['fill'] = (255,69,0)
                x=1485 
                y=20+count*47
                textDict['xy'] = (x,y)
                textList.append(textDict)
                count += 1 #每次设置完毕单词次数加1
                
            elif(length > 3):
                word0 = wordList[0]
                word1 = wordList[2]+wordList[3]
                text = word0+" "+word1
                textDict["text"] = text 
                textDict['fill'] = (46,139,87)
                x=1485
                y=20+count*47
                textDict['xy'] = (x,y)
                textList.append(textDict)
                count += 1
                #print(length)
            elif(length < 3 and length > 1):
                word0 = wordList[0]
                word1 = wordList[1]
                text = word0+" "+word1
                textDict["text"] = text
                textDict['fill'] = (248,248,255)
                x=1485
                y=20+count*47
                textDict['xy'] = (x,y)
                textList.append(textDict)
                count += 1
                #print(text)
            else:
                 print("error")
    #print(textList)
    #print(len(textList))
def writeImage(backgroundImage,textList):
    """
    textList = [{"xy":(100,300),"text":"hello","fill"=(255,255,255)},{......}]
    """
    bk_img = cv2.imread(backgroundImage)

    #设置需要显示的字体
    fontpath = "font/simsun.ttc" #set font.
    font = ImageFont.truetype(fontpath, 32) #set font size
    
    img_pil = Image.fromarray(bk_img) #把图片对象转为图片内存
    draw = ImageDraw.Draw(img_pil) #把图片内存画出来

    #绘制文字信息
   
   
    for text in textList:
        draw.text(text['xy'],text['text'], font = font, fill =text['fill'])
            #draw.text((100, 350),  "你好", font = font, fill = (255, 255, 255))
    
    bk_img = np.array(img_pil)

    cv2.imshow("text6",bk_img)
    cv2.waitKey()
    cv2.imwrite("text6.jpg",bk_img)    

read2List(file)
now = textList[0:20]
random.shuffle(now)
#print(now)
writeImage(image,now)