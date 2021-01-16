# -*- coding: utf-8 -*-
"""
Created on Thu Dec 24 12:25:09 2020

@author: truet
"""
from django.urls import path
from django.conf.urls import url
from . import views
from .views import Home, TagDetailView, CreateTag, UpdateTag, DeleteTag

urlpatterns = [
    path('', Home.as_view(), name='homepage'),
    path('tag/<int:pk>', TagDetailView.as_view(), name='tag_display'),
    path('signup/', views.signup, name='signup'),
    path("create_tag/", CreateTag.as_view(), name='create_tag'),
    path("tag/update/<int:pk>", UpdateTag.as_view(), name='update_tag'),
    path("tag/delete/<int:pk>", DeleteTag.as_view(), name='delete_tag'),
    path("update_profile/", views.update_profile, name='profile'),
]

