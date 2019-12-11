#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 09:47:17 2019

@author: reocar
"""

from django.conf.urls import url
from app_mongo import views

urlpatterns = [
    url(r'^$', views.parse_text),
]