# -*- coding: utf-8 -*-
from django.shortcuts import render

from rest_framework.generics import ListCreateAPIView
from rest_framework import generics
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication

from django.contrib.gis.measure import D
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance

import traceback
import sys

from markets.models import Category, Market, Telephone, Product
from api.serializers.serializer_markets import CategorySerializer, MarketSerializer, TelephoneSerializer, ProductSerializer



class ProductListTableAPIView(APIView):
    """
    API endpoint for products
    """
    
    def get(self, request, id_market, version, format=None):      
        """
        Return a list of market products.
        """     
        id_market = int(id_market)
        
        queryset = Product.objects.filter(market=id_market).order_by('-creation_date')
        serializer = ProductSerializer(queryset, many=True, context={"request":request})
        
        return Response(serializer.data, status=status.HTTP_200_OK)
    
   

class ProductListAPIView(APIView):
    """
    API endpoint for products
    """    
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request, id_market, version, format=None):      
        """
        Return a list of market products.
        """     
        id_market = int(id_market)
        
        queryset = Product.objects.filter(market=id_market, status=1).order_by('-creation_date')
        serializer = ProductSerializer(queryset, many=True, context={"request":request})
        
        return Response({"success":True, "data": serializer.data, "message": "Datos obtenidos correctamente"}, status=status.HTTP_200_OK)