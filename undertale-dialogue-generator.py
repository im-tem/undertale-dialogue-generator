from PIL import *
from PIL import Image,ImageFont,ImageDraw
DELTARUNEBORDER="PATH_TO_BORDER"
fnt=""
def initfont():
    global fnt
    fnt=ImageFont.truetype(fontpath,fontsize)
def gifsave(wholeanim,dur,saveto):
    wholeanim[0].save(saveto,format='GIF',append_images=wholeanim[1:],save_all=True,duration=dur,loop=1)
def strtolist(string):
    emptylist=[]
    emptylist.append(string)
    return emptylist
def createundertaledialog(face,hoffset,fnt,phrase,style):
    img=Image.new('RGB',(512,128),color=(255,255,255))
    ti=Image.open(face)
    draw=ImageDraw.Draw(img)
    if style=="deltarune":
        fontsize=24
        initfont()
        background=Image.open(DELTARUNEBORDER)
        img.paste(background,(0,0))
        voffset=22
    else:
        fontsize=32
        initfont()
        voffset=16
        draw.rectangle(((5,5),(511-6,127-6)),fill="black",outline=None)
    img.paste(ti,(hoffset,16))
    draw.text((116,voffset),phrase,font=fnt,fill=(255,255,255))
    return img
def dialoganim(faces,hoffset,fnt,phrase,style):
    curphrase=''
    phrasetoshow=[]
    for i in phrase:
        curphrase=curphrase+i
        phrasetoshow.append(curphrase)
    for i in range(10):
        phrasetoshow.append(phrase)
    faces_new=[]
    frames=[]
    for i in faces:
        for r in range(2):
            faces_new.append(i)
    faceframe=-1
    for i in phrasetoshow:
        maxframe=len(faces_new)-1
        if faceframe!=maxframe:
            faceframe=faceframe+1
        else:
            faceframe=0
        pic=createundertaledialog(faces_new[faceframe],hoffset,fnt,i,style)
        frames.append(pic)
    return frames
fontpath='PATH_TO_DETERMINATION_MONO'
sansfontpath='PATH_TO_SANS_FONT'
papyrusfontpath='PATH_TO_PAPYRUS_FONT'
fontsize=32
#fnt=ImageFont.truetype(fontpath,fontsize)
sansfnt=ImageFont.truetype(sansfontpath,fontsize)
papyrusfnt=ImageFont.truetype(papyrusfontpath,fontsize)
# Example of creating an animated dialogue is below:
#hoffset=14
#sansfaces=['/home/user/sans1.png','/home/user/sans2.png','/home/user/sans3.png','/home/user/sans4.png','/home/user/sans5.png']
#sans1=dialoganim(strtolist(sansfaces[0]),hoffset,sansfnt,'* hi\nname\'s sans','deltarune')
#sans2=dialoganim(strtolist(sansfaces[2]),hoffset,sansfnt,'* sans the skeleton','deltarune')
#sansanim=sans1+sans2
#gifsave(sansanim,75,'/home/user/sansanimation.gif')
