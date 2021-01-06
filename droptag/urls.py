# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 12:25:09 2020

@author: truet
"""
from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('signup/', views.signup, name='signup'),
    path("form_detail/", views.form_detail, name='form_detail'),
]

