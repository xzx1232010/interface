#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 29 14:06:19 2018

@author: reocar
"""

import dlib
import cv2
import numpy as np
predictor_path='/home/xiasan/face/shape_predictor_68_face_landmarks.dat'
face_rec_model_path='/home/xiasan/face/dlib_face_recognition_resnet_model_v1.dat'
class face_model:  
    #初始化模型
    def __init__(self):
        
        self.detector = dlib.get_frontal_face_detector()
        self.shape_predictor=dlib.shape_predictor(predictor_path)   
        self.face_rec_model=dlib.face_recognition_model_v1(face_rec_model_path)     
    #旋转图片80度
    def rotate_180_pic(self,mat):
        def fz(a):
            return a[::-1]
        return np.array(fz(list(map(fz, mat))))
        
    def face_detect(self,img):   
        dets = self.detector(img, 1)    
        if(len(dets)==0):   
            img_=self.rotate_180_pic(img)#180度旋转
            dets = self.detector(img_, 1)
            if(len(dets)!=0):
                flag='mirror_true'   
            else:
                img_=np.rot90(img)#逆时针旋转90度
                dets = self.detector(img_, 1)
                if(len(dets)!=0):
                    flag=True
                else:
                    img_=np.rot90(img,-1)#顺时针旋转90度
                    dets = self.detector(img_, 1)
                    if(len(dets)!=0):
                        flag='reverse_true'           
                    else:
                        return None,'detect_fail'
        else:
            flag=False
        return dets,flag

    def extract_face_features(self,img,dets,flag):   
        b, g, r = cv2.split(img)
        img_rgb= cv2.merge([r, g, b])    
        if(len(dets)==0):
            return None
        else:
            pass  
        if(flag==True):
            image=np.rot90(img_rgb).copy()
        elif(flag=='reverse_true'):
            image=np.rot90(img_rgb,-1).copy()    
        elif(flag=='mirror_true'):
            image=self.rotate_180_pic(img_rgb).copy()
        else:
            image=img_rgb.copy()   
        face_vector_list=[]
        for index, face in enumerate(dets):
            shape = self.shape_predictor(image, face)
            face_vector = self.face_rec_model.compute_face_descriptor(image, shape)  
            face_vector_list.append(face_vector)    
        return face_vector_list

    def comparePersonData(self,data1, data2):
        diff = 0
        for i in range(len(data1)):
            diff += (data1[i] - data2[i])**2
        diff = np.sqrt(diff)
        return diff
    
    def face_recognize(self,ID_pic,half_length_pic):
        output={}
        dets,flag=self.face_detect(ID_pic) 
        if(dets == None):
            width=ID_pic.shape[1]  
            pic=cv2.resize(ID_pic, (width, width), interpolation=cv2.INTER_CUBIC)    
            dets,flag=self.face_detect(pic) 
            if(dets == None):
                output['ID_fail_reason']=401#身份证识别失败
            else:
                li_=self.extract_face_features(pic,dets,flag)  
                output['ID_fail_reason']=200#身份证识别成功
        else:
            li_=self.extract_face_features(ID_pic,dets,flag) 
            output['ID_fail_reason']=200           
        #半身照转向量
        dets,flag=self.face_detect(half_length_pic)
        if(dets == None):
            output['half_fail_reason']=401#半身照识别失败
        else:        
            xi_=self.extract_face_features(half_length_pic,dets,flag)
            output['half_fail_reason']=200#半身照识别成功        
        #开始比对人脸
        if(output['half_fail_reason']==200 and output['ID_fail_reason']==200):
            compare=[]
            for l in range(len(xi_)):      
                li=np.array(li_[0])      
                xi=np.array(xi_[l])  
                compare.append(self.comparePersonData(xi, li))
            
            if(min(compare)>0.474):
                output['recognize']=False
            else:
                output['recognize']=True
            output['distince']=min(compare)          
            return output
        else:
            return output
            
            
    
    
    
    
    
    
