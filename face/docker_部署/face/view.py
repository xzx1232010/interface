#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 17:07:49 2018

@author: reocar
"""

from django.http import HttpResponse
from django.core.serializers.json import json
import base64
import numpy as np
import cv2
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate

import sys
sys.path.append('/home/xiasan/face/face')
from model import face_model

def base64_to_image(base64_code):
    img_data = base64.b64decode(base64_code)
    img_array = np.fromstring(img_data, np.uint8)
    img = cv2.imdecode(img_array, cv2.COLOR_RGB2BGR)#BGR  
    return img

def face_recognize(ID_pic,half_pic):  
    face=face_model() 
    output=face.face_recognize(ID_pic,half_pic)   
    return output

@csrf_exempt
def post(request):
    if(request.method == 'POST'):
        username=request.POST.get('username','')
        password=request.POST.get('password','')
        user=authenticate(username=username,password=password)
        if(user is not None and user.is_active):
            if(request.POST.get('ID_pic') is not None and request.POST.get('half_pic') is not None):
                ID_pic=request.POST.get('ID_pic')
                ID_pic = base64_to_image(ID_pic)
                
                half_pic=request.POST.get('half_pic')
                half_pic = base64_to_image(half_pic) 
                
                dic = face_recognize(ID_pic,half_pic)
                dic = json.dumps(dic, ensure_ascii=False)
                
                return HttpResponse(dic, content_type='application/json; charset=utf-8')
            else:
                return HttpResponse('Invalid picture')
        else:
            return HttpResponse('Invalid login')
    else:
        return HttpResponse('error method')






