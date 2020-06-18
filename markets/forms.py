#-*- coding: utf-8 -*-
from django import forms
from django.contrib.gis import forms
from django.contrib.gis.geos import Point

from markets.models import Market

class ProductForm(forms.Form):
    title = forms.CharField(max_length = 200)
    description = forms.CharField(max_length = 500)
    price = forms.FloatField()
    file = forms.ImageField()   
    
class MarketForm(forms.Form):
    name_kyper = forms.CharField(max_length=200)
    addresses = forms.CharField(max_length=200) 
    number = forms.CharField(max_length=150)   
    city = forms.CharField(max_length=150)
    minimum_price = forms.FloatField()
    file = forms.ImageField(required=False) 
    delivery_price = forms.FloatField()
    location = forms.PointField(label='Selecciona la ubicación del comercio en el mapa', required=True)
    category = forms.IntegerField()
