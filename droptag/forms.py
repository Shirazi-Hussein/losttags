# -*- coding: utf-8 -*-
"""
Created on Sat Dec 26 20:40:28 2020

@author: truet
"""
from django import forms 
from .models import tag 
  
class tagForm(forms.ModelForm): 
    class Meta: 
        model = tag
        fields = ['tag_name', 
        'id_link', 
        'geo_location', 
        'time_met'
        ] 

