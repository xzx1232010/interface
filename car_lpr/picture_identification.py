#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 16:35:55 2018

@author: reocar
"""
import os
import base64
from hyperlpr import HyperLPR_PlateRecogntion

import numpy as np
import cv2
import shutil


filename=os.listdir('./lpr_pic')

output={}
output_={}
for i in range(len(filename)):
    
    if(filename[i]=='.DS_Store'):
        continue
    path="/Users/reocar/Documents/interface/lpr_pic/"+filename[i]   
    image = cv2.imread(path)
    def image_to_base64(image_np): 
        image = cv2.imencode('.jpg',image_np)[1]
        image_code = str(base64.b64encode(image))[2:-1] 
        return image_code   
    def base64_to_image(base64_code):
        img_data = base64.b64decode(base64_code)
        img_array = np.fromstring(img_data, np.uint8)
        img = cv2.imdecode(img_array, cv2.COLOR_RGB2BGR)
        return img
    aa=image_to_base64(image)
    data={}
    data['image']=aa
    bb=base64_to_image(data['image'])
    
    #print(HyperLPR_PlateRecogntion(bb)[0][0],filename[0].strip('.jpg'))
    
    temp=[bb.shape]
    
    if(len(HyperLPR_PlateRecogntion(bb))==0):
        shutil.copyfile(path,"/Users/reocar/Documents/interface/lost_pic/"+filename[i])
        output_[filename[i].strip('.jpg')]=temp
        continue        
    if(len(HyperLPR_PlateRecogntion(bb)[0][0])!=7):
        temp.append(HyperLPR_PlateRecogntion(bb)[0][0][0:7])
    else:
        temp.append(HyperLPR_PlateRecogntion(bb)[0][0])
    output[filename[i].strip('.jpg')]=temp

    






