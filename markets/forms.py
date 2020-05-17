#-*- coding: utf-8 -*-
from django import forms

class ProductForm(forms.Form):
    title = forms.CharField(max_length = 200)
    description = forms.CharField(max_length = 500)
    price = forms.FloatField()
    file = forms.ImageField()   