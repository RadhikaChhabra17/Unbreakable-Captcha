#this is main script that will run till u quit or interupt it 
#!pip install pillow #for image creating 
import random
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import os
print("running statup script ")
def sucess():
    print("u are clear to go ")
    quit()
def loadf1():
    path=os.path.join(os.getcwd(),"resource/file1.txt")     
    file = open(path,'r')  
    content = file.readlines()
    __n1__=random.randint(0, len(content)-1)
    str=content[__n1__]
    str=str.split(",")
    ran=random.randint(0, len(str)-1)
    text=""
    for x in enumerate(str,start=0):
        if(x[0]!=ran):
         #print(x[1],end=",")
         text+=x[1]+","
        else : 
            #print("__",end=",")
            text+="__"+","
    print(text)
    plotim(text)
    inp=input("your best guess for blank is :")
    if(inp==str[ran]):
      sucess()
    else:print("press any key to exit retry new one ") 
def plotim(str):
    txt=str #input text 
    img =Image.new('RGB',(150,50),color=(73,100,107))
    fontsize=18
    image_fraction=0.5
    font=ImageFont.truetype('fonts/Roboto-Bold.ttf',fontsize)
    while font.getsize(txt)[0]<image_fraction*img.size[0]:
            fontsize+=1
            font=ImageFont.truetype('fonts/Roboto-Bold.ttf',fontsize)
    fontsize-=1
    # print(fontsize)

    draw=ImageDraw.Draw(img)       
    draw.text((10,10), txt,font=ImageFont.truetype('fonts/Roboto-Bold.ttf',fontsize)) 
    
    # draw = ImageDraw.Draw(img)
    # font = ImageFont.truetype(r'filepath\..\sans-serif.ttf', 16)
    # draw.text((0, 0),"Draw This Text",(0,0,0),font=font) # this will draw text with Blackcolor and 16 size
    
    img.save('out.jpg')
    
while True:
    print(">",end="")
    ##loop part runs indefinately 
    num=random.randint(0,5)
    if(num==1):
        ##callback 1 type of captcha ##
        loadf1()
    if(num==2):
        ##callback to loadf2### 
        print("hi")   
    if(num==3):
        ##callback to loadf3###
        print("hi")
    if(num==4):
        ## callback to loaf4###    
        print("hi")
    if(num==5):
        ##callback to loaf5###
        print("hi")
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    inpt=input("press q to exit ")

    if(inpt=="q"or inpt=="Q"):
     print("quiting")
     quit() 
