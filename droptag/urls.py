# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 12:25:09 2020

@author: truet
"""
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='homepage'),
    url('signup/', views.signup, name='signup'),
]

