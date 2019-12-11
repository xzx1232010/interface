#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 16:35:55 2018

@author: reocar
"""

import base64
import cv2
import requests
import os
from PIL import Image
import random
import time
#import math 

def show_pic(pic):
    cv2img=cv2.cvtColor(pic,cv2.COLOR_BGR2RGB)
    pilimg=Image.fromarray(cv2img)
    pilimg.show()
    
def image_to_base64(image_np): 
    image = cv2.imencode('.jpg',image_np)[1]
    image_code = str(base64.b64encode(image))[2:-1] 
    return image_code

def shrink_pic(pic):   
    height,width = pic.shape[:2] 
    size = (width, height) 
    if(max(size)>800):
        scale=round(max(pic.shape[:2])/800,1)
        size = (int(width/scale), int(height/scale)) 
    else:
        pass    
    if(min(size)<400):
        scale=round(min(pic.shape[:2])/400,1)
        size = (int(width/scale), int(height/scale))       
    else:
        pass    
    pic = cv2.resize(pic, size, interpolation=cv2.INTER_AREA) 
    return pic
    
def main():
    
    path_list=os.listdir('/Users/reocar/Documents/face/verify_pic')
    id_num=random.randrange(len(path_list))
    half_num=random.randrange(len(path_list))

    ID_pic=cv2.imread('/Users/reocar/Documents/face/verify_pic/'+path_list[id_num]+'/ID.jpg')
    half_pic=cv2.imread('/Users/reocar/Documents/face/verify_pic/'+path_list[id_num]+'/half.jpg')
    
    ID_pic=shrink_pic(ID_pic)
    half_pic=shrink_pic(half_pic)

    show_pic(ID_pic)
    show_pic(half_pic)
    
    ID_pic=ID_pic[...,::-1]#RGB格式
    half_pic=half_pic[...,::-1]#RGB格式
    
    data={}
    
    data['ID_pic']=image_to_base64(ID_pic)
    data['half_pic']=image_to_base64(half_pic)
    
    data['username']='reocar'
    data['password']='reocar666'

    #url='http://192.168.15.77:58010/face/'

    url='http://face-recognize9.stagpx.reocar.com/face/'
    
    start=time.time()
    res = requests.post(url=url,data=data)   
    
    answer=res.json()
    end=time.time()
    print(ID_pic.shape,half_pic.shape)
    
    ID_pic=shrink_pic(ID_pic)
    half_pic=shrink_pic(half_pic)
    
    print(end-start,ID_pic.shape,half_pic.shape)
    print(answer)
    
    return answer

main()





