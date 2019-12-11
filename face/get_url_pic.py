#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 20 09:54:00 2019

@author: reocar
"""

import requests
from PIL import Image
from io import BytesIO

data={}

data['member_id']='00033249-07e8-449b-ac3c-394d84c03749'

url='http://store.reocar.com/services/members/document_images?'

res = requests.get(url=url,params=data)

answer=res.json()

half_length_photo=answer['data']['avatar']

valida_license=answer['data']['validated_license']
non_valida_license=answer['data']['non_validated_license']

id_card_front=valida_license['身份证件正面']

non_id_card_front=non_valida_license['身份证件正面']


response = requests.get(id_card_front)
image = Image.open(BytesIO(response.content))
image.show()


import numpy as np
import urllib
import cv2
resp = urllib.request.urlopen(half_length_photo)
img = np.asarray(bytearray(resp.read()), dtype="uint8")

img = cv2.imdecode(img, cv2.IMREAD_COLOR)

cv2.imshow("Image", img)
cv2.waitKey(0)





