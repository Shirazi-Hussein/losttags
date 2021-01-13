# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 20:40:28 2020

@author: truet
"""
from django import forms 
from .models import tag, UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
  
class tagForm(forms.ModelForm): 
    class Meta: 
        model = tag
        fields = ['platform',
        'username', 
        'id_link',  
        'time_met',
        'note'
        ]
        

class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('name', 'id_link', 'about')

