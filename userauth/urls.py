# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 18:51:56 2021

@author: truet
"""
from django.urls import path
from django.conf.urls import url
from .views import UserRegisterView


urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
]



