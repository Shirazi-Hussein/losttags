# -*- coding: utf-8 -*-
"""
Created on Sun Jan 17 18:51:56 2021

@author: truet
"""
from django.urls import path
from django.conf.urls import url
from .views import UserEditView, ChangePasswordView
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    #path('register/', UserRegisterView.as_view(), name='register'),
    path('edit_profile/', UserEditView.as_view(), name='edit_profile'),
    path('password/', ChangePasswordView.as_view(), name='change_password'),
    #path('password_success', views.password_success, name='password_success')
]



