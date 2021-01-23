# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 20:40:28 2020

@author: truet
"""
from django import forms 
import django.forms.widgets
from .models import tag, UserProfile
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
  
class tagForm(forms.ModelForm): 
    class Meta: 
        model = tag
        fields = ['user',
        'platform',
        'username', 
        'id_link',  
        'time_met',
        'note'
        ]
         
        widgets = {
            'user': forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'user_js', 'type':'hidden'}),
            'platform': forms.Select(attrs={'class':'form-control'}),
            'username': forms.TextInput(attrs={'class':'form-control', 
                                               'placeholder':'Steam Name, Gamertag, Full Discord Tag, Or PSN Username'}),
            'id_link': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Link To Account (optional)'}),
            'time_met': forms.DateInput(attrs={'class':'form-control', 'placeholder':'When Did You Meet Them?'}),
            'note': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Extra Information (optional)'}),
            }
        

class UpdateTagForm(forms.ModelForm): 
    class Meta: 
        model = tag
        fields = [
        'username', 
        'id_link',  
        'time_met',
        'note'
        ]
         
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control', 
                                               'placeholder':'Steam Name, Gamertag, Full Discord Tag, Or PSN Username'}),
            'id_link': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Link To Account (optional)'}),
            'time_met': forms.DateInput(attrs={'class':'form-control', 'placeholder':'When Did You Meet Them?'}),
            'note': forms.Textarea(attrs={'class':'form-control', 'placeholder':'Extra Information (optional)'}),
            }
        
        
        
        
        
        
class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', )


class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('name', 'id_link', 'about')

