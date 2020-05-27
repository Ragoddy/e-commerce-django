#-*- coding: utf-8 -*-
from django import forms

class OrderForm(forms.Form):
    payment_method = forms.IntegerField()
    comments = forms.CharField(max_length=500,  required=False)    
    address = forms.CharField(max_length=200) 
    complement_address = forms.CharField(max_length=200,  required=False) 
    name_client = forms.CharField(max_length=200) 
    phone = forms.CharField(max_length=200,  required=False) 