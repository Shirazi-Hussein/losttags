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
        'geo_location', 
        'time_met',
        'note'
        ]
        

class SignUpForm(UserCreationForm):
    name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    id_link = forms.CharField(max_length=30, required=False, help_text='Optional.')
    about = forms.CharField(max_length=254, required=False, help_text='Enter any additional information.')

    class Meta:
        model = User
        fields = ('username', 'name', 'id_link', 'about', 'password1', 'password2', )


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('id_link', 'about')

