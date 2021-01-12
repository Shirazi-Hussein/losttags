# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 12:25:09 2020

@author: truet
"""
from django.urls import path
from django.conf.urls import url
from . import views
from .views import Home, TagDetailView

urlpatterns = [
    path('', Home.as_view(), name='homepage'),
    path('tag/<int:pk>', TagDetailView.as_view(), name='tag_display'),
    path('signup/', views.signup, name='signup'),
    path("form_detail/", views.form_detail, name='form_detail'),
    path("update_profile/", views.update_profile, name='profile')
]

