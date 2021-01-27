# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 20:40:28 2020

@author: truet
"""
from django import forms 
from .models import tag, UserProfile
from django.contrib.auth.forms import UserCreationForm
  
class tagForm(forms.ModelForm): 
    class Meta: 
        model = tag
        fields = ['platform',
        'username', 
        'id_link',  
        'time_met',
        'note'
        ]
         
        widgets = {
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


class UserProfileForm(UserCreationForm):
    class Meta:
        model = UserProfile
        fields = ['name',
                  'steam_id', 
                  'psn_id', 
                  'xbox_id', 
                  'discord_id', 
                  'bio'
                  ]
        
        widgets = {}
        
        
        
        

