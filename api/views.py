# -*- coding: utf-8 -*-
from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import permissions

from markets.models import Category, Market

from api.serializers import CategorySerializer, MarketSerializer

class CategoryListAPIViewSet(generics.ListAPIView):
    """
    API endpoint for categories app.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    
class MarketListAPIViewSet(generics.ListCreateAPIView):
    """
    API endpoint for categories app.
    """
    queryset = Market.objects.all()
    serializer_class = MarketSerializer
